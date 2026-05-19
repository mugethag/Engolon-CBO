import os
import json
from datetime import date
from pathlib import Path
from integrations.claude_client import complete
from integrations.sheets import append_rows, read_rows
from utils.logger import get_logger

logger = get_logger(__name__)

_SYSTEM = """You are a brand strategist analyzing a community organization's website.
Extract a brand voice profile as JSON with exactly these keys:
{
  "mission": "one sentence mission statement",
  "tone": "comma-separated tone adjectives (e.g. warm, hopeful, dignified)",
  "audience": "primary audience description",
  "content_pillars": ["pillar1", "pillar2", "pillar3", "pillar4"],
  "fundraising_style": "how the org appeals to donors",
  "hook_patterns": ["hook pattern 1", "hook pattern 2", "hook pattern 3"]
}
Return ONLY valid JSON. No markdown, no explanation."""


def run(spreadsheet_id: str, website_content: str) -> dict:
    """Extract brand voice profile from website content and write to Sheets."""
    logger.info("brand_agent: building brand voice profile")

    raw = complete(
        system=_SYSTEM,
        user=f"Analyze this organization website and extract a brand voice profile:\n\n{website_content[:8000]}"
    )
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1].lstrip("json").strip()
    try:
        profile = json.loads(raw)
    except json.JSONDecodeError as e:
        logger.error(f"brand_agent: Claude returned invalid JSON: {e}\nRaw (first 300 chars): {raw[:300]}")
        raise

    row = [
        str(date.today()),
        "1.0",
        profile.get("mission", ""),
        profile.get("tone", ""),
        profile.get("audience", ""),
        ", ".join(profile.get("content_pillars", [])),
        profile.get("fundraising_style", ""),
        ", ".join(profile.get("hook_patterns", [])),
    ]
    append_rows(spreadsheet_id, "Brand Voice Profile", [row])

    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)
    (data_dir / "brand_profile.json").write_text(json.dumps(profile, indent=2))

    logger.info("brand_agent: done")
    return profile


def load_brand_profile(spreadsheet_id: str) -> dict:
    """Load the most recent brand profile row from Sheets."""
    rows = read_rows(spreadsheet_id, "Brand Voice Profile")
    if len(rows) < 2:
        raise ValueError("No brand profile in Sheets. Run brand_agent first via the setup workflow.")
    last = rows[-1]

    def safe(idx, default=""):
        return last[idx] if len(last) > idx else default

    return {
        "mission": safe(2),
        "tone": safe(3),
        "audience": safe(4),
        "content_pillars": [p.strip() for p in safe(5).split(",") if p.strip()],
        "fundraising_style": safe(6),
        "hook_patterns": [p.strip() for p in safe(7).split(",") if p.strip()],
    }


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    website = Path(__file__).parent.parent.parent / "index.html"
    run(os.environ['SPREADSHEET_ID'], website.read_text(encoding='utf-8'))
