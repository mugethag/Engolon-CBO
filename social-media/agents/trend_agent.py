import os
import json
from datetime import date
from collections import defaultdict
from integrations.sheets import read_rows, append_rows
from integrations.llm_client import complete
from utils.logger import get_logger
from utils.retry import with_retry

logger = get_logger(__name__)

OUTLIER_THRESHOLD_LARGE = 2.5   # creators >= 10k subscribers
OUTLIER_THRESHOLD_SMALL = 1.8   # creators < 10k subscribers


def calculate_outlier_scores(videos: list) -> list:
    """Calculate outlier score for each video vs. that creator's average views."""
    by_creator = defaultdict(list)
    for v in videos:
        by_creator[v["creator_name"]].append(v["views"])

    avgs = {name: sum(vs) / len(vs) for name, vs in by_creator.items()}

    enriched = []
    for v in videos:
        avg = avgs[v["creator_name"]]
        score = round(v["views"] / avg, 2) if avg > 0 else 0.0
        threshold = OUTLIER_THRESHOLD_SMALL if v.get("subscriber_count", 0) < 10000 else OUTLIER_THRESHOLD_LARGE
        enriched.append({**v, "creator_avg": avg, "outlier_score": score, "threshold": threshold})

    return enriched


@with_retry(max_attempts=3, base_delay=2.0)
def _enrich(video: dict) -> dict:
    """Use the LLM to extract patterns from an outlier video."""
    prompt = f"""A video is significantly outperforming its creator's average.

Creator: {video['creator_name']} ({video.get('subscriber_count', 0):,} subscribers)
Title: {video['title']}
Views: {video['views']:,} (creator avg: {video['creator_avg']:,.0f}) — {video['outlier_score']}x

Analyze in JSON:
{{
  "hook_pattern": "the likely hook/opening pattern",
  "emotional_trigger": "the core emotional driver",
  "why_it_works": "2-3 sentence explanation",
  "adaptation_idea": "how Engolon CBO (serving women, children, elderly, PWDs in Kibra Kenya) can create original content using this pattern for donor acquisition"
}}
Return ONLY valid JSON."""

    raw = complete(
        system="You are a social media strategist specializing in NGO/nonprofit content for East Africa.",
        user=prompt
    )
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1].lstrip("json").strip()
    try:
        return {**video, **json.loads(raw)}
    except json.JSONDecodeError as e:
        logger.error(f"_enrich: OpenAI returned invalid JSON: {e}\nRaw (first 300 chars): {raw[:300]}")
        raise


def run(spreadsheet_id: str) -> list:
    """Detect outlier videos and enrich them with LLM analysis."""
    logger.info("trend_agent: starting")
    rows = read_rows(spreadsheet_id, "Competitor Tracking")

    if len(rows) < 2:
        logger.warning("trend_agent: no competitor data found — run research_agent first")
        return []

    videos = []
    for row in rows[1:]:
        if len(row) < 8:
            continue
        try:
            videos.append({
                "creator_name": row[2],
                "subscriber_count": int(row[3]) if row[3] else 0,
                "url": row[4],
                "title": row[5],
                "views": int(row[7]) if row[7] else 0,
            })
        except (ValueError, IndexError):
            continue

    scored = calculate_outlier_scores(videos)
    outliers = sorted(
        [v for v in scored if v["outlier_score"] >= v["threshold"]],
        key=lambda x: x["outlier_score"],
        reverse=True
    )
    logger.info(f"trend_agent: {len(outliers)} outliers from {len(scored)} videos")

    enriched = []
    for v in outliers[:10]:  # cap at 10 LLM calls per run
        try:
            enriched.append(_enrich(v))
        except Exception as e:
            logger.error(f"trend_agent: enrichment failed for '{v['title']}': {e}")
            enriched.append(v)

    today = str(date.today())
    out_rows = [[
        today,
        v["creator_name"],
        v["url"],
        v["title"],
        v.get("hook_pattern", ""),
        v.get("why_it_works", ""),
        v.get("emotional_trigger", ""),
        v.get("adaptation_idea", ""),
        "pending",
    ] for v in enriched]

    if out_rows:
        append_rows(spreadsheet_id, "Trend Outliers", out_rows)
        logger.info(f"trend_agent: wrote {len(out_rows)} outliers to Trend Outliers")

    return enriched


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    run(os.environ['SPREADSHEET_ID'])
