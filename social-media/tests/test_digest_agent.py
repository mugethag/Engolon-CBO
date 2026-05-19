import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from agents.digest_agent import build_email_html

def _outlier_row(title="Big Impact", creator="SHOFCO", url="https://yt.com/x",
                 emotional="hope", adaptation="Focus on Kibra youth"):
    return ["2026-05-19", creator, url, title, "hook", "why", emotional, adaptation, "pending"]

def _script_row(platform="Facebook/Instagram", hook="One child at a time",
                caption="Support us today.", cta="Donate at [DONATE_LINK]"):
    return ["2026-05-19", platform, hook, caption, "point1 | point2", cta, "s1 | s2", "Draft"]

def test_html_contains_outlier_title():
    html = build_email_html([_outlier_row()], [], [])
    assert "Big Impact" in html

def test_html_contains_script_hook():
    html = build_email_html([], [_script_row()], [])
    assert "One child at a time" in html

def test_html_shows_errors():
    html = build_email_html([], [], ["YouTube API quota exceeded"])
    assert "YouTube API quota exceeded" in html

def test_html_handles_empty_inputs():
    html = build_email_html([], [], [])
    assert "No outliers found today" in html
    assert "No scripts generated today" in html

def test_html_caps_at_3_outliers():
    rows = [_outlier_row(title=f"Video {i}") for i in range(5)]
    html = build_email_html(rows, [], [])
    assert html.count("Video") == 3  # only first 3 shown
