import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from agents.trend_agent import calculate_outlier_scores, OUTLIER_THRESHOLD_LARGE, OUTLIER_THRESHOLD_SMALL

def _make_video(creator, views, subscribers=50000):
    return {"creator_name": creator, "views": views, "subscriber_count": subscribers,
            "title": "Test", "url": "https://youtube.com/watch?v=x"}

def test_outlier_score_is_ratio_vs_creator_avg():
    videos = [
        _make_video("Org A", 100),
        _make_video("Org A", 200),
        _make_video("Org A", 1000),  # avg = 433; score = 1000/433 ≈ 2.31
    ]
    scored = calculate_outlier_scores(videos)
    avg = (100 + 200 + 1000) / 3
    expected = round(1000 / avg, 2)
    assert scored[2]["outlier_score"] == expected

def test_zero_views_scores_zero():
    videos = [_make_video("Org A", 0), _make_video("Org A", 0)]
    scored = calculate_outlier_scores(videos)
    assert scored[0]["outlier_score"] == 0

def test_small_creator_threshold_is_lower():
    videos = [_make_video("Small", 100, subscribers=5000),
              _make_video("Small", 100, subscribers=5000)]
    scored = calculate_outlier_scores(videos)
    assert scored[0]["threshold"] == OUTLIER_THRESHOLD_SMALL

def test_large_creator_threshold_is_higher():
    videos = [_make_video("Big", 100, subscribers=50000),
              _make_video("Big", 100, subscribers=50000)]
    scored = calculate_outlier_scores(videos)
    assert scored[0]["threshold"] == OUTLIER_THRESHOLD_LARGE

def test_isolates_creators():
    videos = [
        _make_video("A", 100), _make_video("A", 100),
        _make_video("B", 1000), _make_video("B", 1000),
    ]
    scored = calculate_outlier_scores(videos)
    a_scores = [v["outlier_score"] for v in scored if v["creator_name"] == "A"]
    b_scores = [v["outlier_score"] for v in scored if v["creator_name"] == "B"]
    # Within same creator, all equal views → all score 1.0
    assert all(s == 1.0 for s in a_scores)
    assert all(s == 1.0 for s in b_scores)
