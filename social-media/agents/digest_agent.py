import os
from datetime import date
from integrations.sheets import read_rows, append_rows
from integrations.gmail import send_html_email
from utils.logger import get_logger

logger = get_logger(__name__)


def build_email_html(outliers: list, scripts: list, errors: list) -> str:
    """Build the HTML body for the daily digest email."""
    today = str(date.today())

    def _outlier_block(row):
        if len(row) < 8:
            return ""
        return f"""
        <div style="border-left:3px solid #2D5016;padding-left:12px;margin-bottom:16px">
          <strong>{row[3]}</strong> — {row[1]}<br>
          <em>Emotional trigger: {row[6]}</em><br>
          <a href="{row[2]}" style="font-size:12px">{row[2]}</a><br>
          <p style="color:#555;margin-top:6px">{row[7]}</p>
        </div>"""

    def _script_block(i, row):
        if len(row) < 6:
            return ""
        caption_preview = row[3][:300] + ("..." if len(row[3]) > 300 else "")
        return f"""
        <div style="background:#f5f1eb;padding:12px;margin-bottom:12px;border-radius:4px">
          <strong>Script {i} — {row[1]}</strong><br>
          <em>Hook:</em> {row[2]}<br>
          <p style="margin:8px 0">{caption_preview}</p>
          <small style="color:#888">CTA: {row[5]}</small>
        </div>"""

    outlier_html = "".join(_outlier_block(r) for r in outliers[:3])
    if not outlier_html:
        outlier_html = '<p style="color:#888">No outliers found today.</p>'

    script_html = "".join(_script_block(i + 1, r) for i, r in enumerate(scripts[:3]))
    if not script_html:
        script_html = '<p style="color:#888">No scripts generated today.</p>'

    error_html = ""
    if errors:
        items = "".join(f"<li>{e}</li>" for e in errors)
        error_html = f'<h3 style="color:#c0392b">Errors ({len(errors)})</h3><ul>{items}</ul>'

    return f"""<html><body style="font-family:Arial,sans-serif;max-width:640px;margin:auto;color:#333;padding:20px">
  <h2 style="color:#2D5016">Engolon CBO — Social Media Digest</h2>
  <p style="color:#888;margin-top:-10px">{today}</p>

  <h3 style="border-bottom:2px solid #C97A4A;padding-bottom:4px">Top Outliers ({len(outliers)})</h3>
  {outlier_html}

  <h3 style="border-bottom:2px solid #C97A4A;padding-bottom:4px">Scripts Ready for Review ({len(scripts)})</h3>
  {script_html}

  {error_html}

  <hr style="margin-top:32px">
  <p style="color:#aaa;font-size:11px">Engolon CBO Automated Marketing System — Phase 1<br>
  Update Channel IDs in the Config tab to improve research coverage.</p>
</body></html>"""


def run(spreadsheet_id: str, errors: list = None) -> None:
    """Compile today's data from all tabs and send the daily digest email."""
    logger.info("digest_agent: starting")
    errors = errors or []
    today = str(date.today())

    def today_rows(tab):
        all_rows = read_rows(spreadsheet_id, tab)
        return [r for r in all_rows[1:] if r and len(r) > 0 and r[0] == today]

    outliers = today_rows("Trend Outliers")
    scripts = today_rows("Scripts")

    html = build_email_html(outliers, scripts, errors)
    subject = (
        f"Engolon Social Digest — {today} "
        f"({len(outliers)} outlier{'s' if len(outliers) != 1 else ''}, "
        f"{len(scripts)} script{'s' if len(scripts) != 1 else ''})"
    )

    send_html_email(subject=subject, html_body=html)

    append_rows(spreadsheet_id, "Daily Digest Archive", [[
        today, subject, len(outliers), len(scripts), "; ".join(errors)
    ]])
    logger.info("digest_agent: email sent and archived")


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    run(os.environ['SPREADSHEET_ID'])
