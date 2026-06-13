import os
import json
from datetime import date
from integrations.sheets import read_rows, append_rows
from integrations.llm_client import complete
from agents.brand_agent import load_brand_profile
from utils.logger import get_logger

logger = get_logger(__name__)

_SYSTEM = """You are a social media content writer for Engolon CBO, a Kenya-based community organization serving vulnerable communities: women, children, the elderly, and persons with disabilities (PWDs).

Primary goal: donor acquisition and fundraising.

Rules:
- Match the brand voice exactly (provided in context)
- NEVER copy reference content — identify the pattern only, generate original content
- Every post must include a clear donor/fundraising call to action
- Speak directly to potential donors with empathy and urgency
- Keep captions conversational and human, 150-250 words"""


def generate_post(outlier: dict, brand: dict) -> dict:
    """Generate an original social media post adapted from an outlier pattern."""
    context = f"""Brand voice: {brand.get('tone', '')}
Mission: {brand.get('mission', '')}
Audience: {brand.get('audience', '')}
Content pillars: {', '.join(brand.get('content_pillars', []))}
Fundraising style: {brand.get('fundraising_style', '')}"""

    prompt = f"""{context}

Reference outlier (learn from the pattern, do NOT copy):
Title: {outlier.get('title', '')}
Hook pattern: {outlier.get('hook_pattern', '')}
Emotional trigger: {outlier.get('emotional_trigger', '')}
Adaptation idea: {outlier.get('adaptation_idea', '')}

Generate an original Engolon CBO social media post as JSON:
{{
  "hook": "opening hook, max 10 words",
  "caption": "full Facebook/Instagram caption (150-250 words, ends with a CTA)",
  "talking_points": ["point 1", "point 2", "point 3"],
  "cta": "specific CTA — include placeholder [DONATE_LINK] where the link goes",
  "carousel_outline": ["slide 1 headline", "slide 2 headline", "slide 3 headline", "slide 4 headline"],
  "suggested_title": "suggested post title for reference"
}}
Return ONLY valid JSON."""

    raw = complete(system=_SYSTEM, user=prompt, max_tokens=1500)
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1].lstrip("json").strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        logger.error(f"generate_post: OpenAI returned invalid JSON: {e}\nRaw (first 300 chars): {raw[:300]}")
        raise


def run(spreadsheet_id: str) -> list:
    """Generate donor-acquisition posts from top outliers and write to Scripts + Content Ideas tabs."""
    logger.info("script_agent: starting")
    brand = load_brand_profile(spreadsheet_id)

    rows = read_rows(spreadsheet_id, "Trend Outliers")
    if len(rows) < 2:
        logger.warning("script_agent: no outliers found — run trend_agent first")
        return []

    today = str(date.today())
    today_outliers = [row for row in rows[1:] if row and len(row) >= 8 and row[0] == today]
    if not today_outliers:
        logger.warning("script_agent: no outliers found for today — run trend_agent first")
        return []

    top_3 = []
    for row in today_outliers[-3:]:
        top_3.append({
            "title":             row[3] if len(row) > 3 else "",
            "hook_pattern":      row[4] if len(row) > 4 else "",
            "why_it_works":      row[5] if len(row) > 5 else "",
            "emotional_trigger": row[6] if len(row) > 6 else "",
            "adaptation_idea":   row[7] if len(row) > 7 else "",
        })

    scripts = []

    for outlier in top_3:
        try:
            post = generate_post(outlier, brand)
            scripts.append(post)

            append_rows(spreadsheet_id, "Scripts", [[
                today,
                "Facebook/Instagram",
                post.get("hook", ""),
                post.get("caption", ""),
                " | ".join(post.get("talking_points", [])),
                post.get("cta", ""),
                " | ".join(post.get("carousel_outline", [])),
                "Draft",
            ]])

            append_rows(spreadsheet_id, "Content Ideas", [[
                today,
                outlier.get("title", ""),
                "Facebook/Instagram",
                post.get("hook", ""),
                post.get("suggested_title", ""),
                "caption",
                "donor acquisition",
                "1",
            ]])

        except Exception as e:
            logger.error(f"script_agent: failed for '{outlier.get('title', '')}': {e}")

    logger.info(f"script_agent: generated {len(scripts)} scripts")
    return scripts


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    run(os.environ['SPREADSHEET_ID'])
