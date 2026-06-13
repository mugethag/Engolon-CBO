import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from dotenv import load_dotenv
load_dotenv()
from integrations.sheets import _get_service, overwrite_range

TABS = {
    "Brand Voice Profile": ["Date", "Version", "Mission", "Tone", "Audience",
                             "Content Pillars", "Fundraising Style", "Hook Patterns"],
    "Competitor Tracking": ["Date", "Platform", "Creator", "Subscriber Count", "Post URL",
                             "Title", "Format", "Views/Likes", "Creator Avg", "Outlier Score"],
    "Trend Outliers":      ["Date", "Creator", "URL", "Title", "Hook Pattern",
                             "Why It Works", "Emotional Trigger", "Adaptation Idea", "Status"],
    "Content Ideas":       ["Date", "Source Outlier", "Platform", "Hook", "Concept Summary",
                             "Format", "Fundraising Angle", "Priority"],
    "Scripts":             ["Date", "Platform", "Hook", "Caption", "Talking Points",
                             "CTA", "Carousel Outline", "Status"],
    "Daily Digest Archive":["Date", "Email Subject", "Outliers Found", "Scripts Generated", "Errors"],
    "Config":              ["Name", "Platform", "Channel ID", "Notes"],
}

# Seed data for Config tab — update Channel IDs after looking them up on YouTube
CONFIG_SEED = [
    ["Kenya Red Cross",  "YouTube", "REPLACE_WITH_CHANNEL_ID", "Kenya Red Cross KE"],
    ["SHOFCO",           "YouTube", "REPLACE_WITH_CHANNEL_ID", "Shining Hope for Communities"],
    ["UNICEF Kenya",     "YouTube", "REPLACE_WITH_CHANNEL_ID", "UNICEF Kenya"],
    ["Amref Health",     "YouTube", "REPLACE_WITH_CHANNEL_ID", "Amref Health Africa"],
    ["GlobalGiving",     "YouTube", "REPLACE_WITH_CHANNEL_ID", "GlobalGiving Stories"],
]

def setup(spreadsheet_id: str) -> None:
    service = _get_service()

    meta = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    existing = {s['properties']['title'] for s in meta['sheets']}

    add_requests = []
    for tab_name in TABS:
        if tab_name not in existing:
            add_requests.append({'addSheet': {'properties': {'title': tab_name}}})

    if add_requests:
        service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={'requests': add_requests}
        ).execute()
        print(f"Created {len(add_requests)} new tab(s)")

    sheets_values = service.spreadsheets().values()
    for tab_name, headers in TABS.items():
        sheets_values.update(
            spreadsheetId=spreadsheet_id,
            range=f"{tab_name}!A1",
            valueInputOption='RAW',
            body={'values': [headers]}
        ).execute()

    config_values = sheets_values.get(
        spreadsheetId=spreadsheet_id,
        range="Config!A2:D",
    ).execute().get("values", [])

    if not config_values:
        sheets_values.append(
            spreadsheetId=spreadsheet_id,
            range="Config!A2",
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body={'values': CONFIG_SEED}
        ).execute()

    print("Setup complete.")
    print("IMPORTANT: Open the Config tab and replace all REPLACE_WITH_CHANNEL_ID values")
    print("with real YouTube channel IDs before running the pipeline.")

if __name__ == '__main__':
    sid = os.environ.get('SPREADSHEET_ID') or sys.argv[1]
    setup(sid)
