import os
from datetime import date
from integrations.youtube import get_channel_recent_videos
from integrations.sheets import append_rows, read_rows
from utils.logger import get_logger

logger = get_logger(__name__)


def _load_competitors(spreadsheet_id: str) -> list:
    """Read YouTube competitors from Config tab columns A (Name), B (Platform), C (Channel ID)."""
    rows = read_rows(spreadsheet_id, "Config", "A:C")
    result = []
    skipped = 0
    for row in rows[1:]:  # skip header
        if len(row) < 3:
            continue
        name, platform, channel_id = row[0], row[1].strip().lower(), row[2].strip()
        if platform == "youtube" and not channel_id.startswith("REPLACE"):
            result.append({"name": name, "channel_id": channel_id})
        elif platform == "youtube" and channel_id.startswith("REPLACE"):
            logger.debug(f"research_agent: skipping unconfigured channel '{name}' — update Channel ID in Config tab")
        else:
            skipped += 1
    if skipped:
        logger.info(f"research_agent: skipped {skipped} non-YouTube entries (X/Twitter not supported in Phase 1)")
    return result


def run(spreadsheet_id: str) -> list:
    """Fetch recent videos from competitor channels and write to Competitor Tracking tab."""
    logger.info("research_agent: starting")
    competitors = _load_competitors(spreadsheet_id)

    if not competitors:
        logger.warning("research_agent: no valid YouTube channels in Config tab — update Channel IDs")
        return []

    logger.info(f"research_agent: monitoring {len(competitors)} channels")
    all_videos = []
    today = str(date.today())

    for comp in competitors:
        try:
            videos = get_channel_recent_videos(comp["channel_id"])
            for v in videos:
                v["creator_name"] = comp["name"]
            all_videos.extend(videos)
            logger.info(f"  {comp['name']}: {len(videos)} videos fetched")
        except Exception as e:
            logger.error(f"  {comp['name']}: FAILED — {e}")

    rows = []
    for v in all_videos:
        rows.append([
            today,
            "YouTube",
            v["creator_name"],
            v.get("subscriber_count", 0),
            v["url"],
            v["title"],
            "video",
            v["views"],
            "",  # creator_avg — calculated by trend_agent
            "",  # outlier_score — calculated by trend_agent
        ])

    if rows:
        append_rows(spreadsheet_id, "Competitor Tracking", rows)
        logger.info(f"research_agent: wrote {len(rows)} rows to Competitor Tracking")
    else:
        logger.warning("research_agent: no videos fetched — Competitor Tracking not updated")

    return all_videos


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    run(os.environ['SPREADSHEET_ID'])
