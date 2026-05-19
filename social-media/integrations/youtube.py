import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from googleapiclient.discovery import build
from utils.retry import with_retry

def _get_service():
    """Build YouTube Data API v3 service using API key."""
    api_key = os.environ.get('YOUTUBE_API_KEY')
    if not api_key:
        raise ValueError("YOUTUBE_API_KEY environment variable is not set")
    return build('youtube', 'v3', developerKey=api_key)

def _safe_int(value, default=0) -> int:
    """Safely convert a value to int, returning default on failure."""
    try:
        return int(value or default)
    except (ValueError, TypeError):
        return default

@with_retry(max_attempts=3, base_delay=2.0)
def get_channel_recent_videos(channel_id: str, max_results: int = 10) -> list:
    """Return list of recent video dicts for a channel, or [] if not found."""
    service = _get_service()

    ch_resp = service.channels().list(
        part='contentDetails,statistics',
        id=channel_id
    ).execute()

    if not ch_resp.get('items'):
        return []

    item = ch_resp['items'][0]
    playlist_id = (item.get('contentDetails', {})
                       .get('relatedPlaylists', {})
                       .get('uploads'))
    if not playlist_id:
        return []

    subscriber_count = _safe_int(item.get('statistics', {}).get('subscriberCount'))

    pl_resp = service.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=max_results
    ).execute()

    video_ids = [
        v['snippet']['resourceId']['videoId']
        for v in pl_resp.get('items', [])
    ]
    if not video_ids:
        return []

    vid_resp = service.videos().list(
        part='snippet,statistics',
        id=','.join(video_ids)
    ).execute()

    videos = []
    for v in vid_resp.get('items', []):
        stats = v.get('statistics', {})
        videos.append({
            'video_id': v['id'],
            'title': v['snippet']['title'],
            'url': f"https://youtube.com/watch?v={v['id']}",
            'views': _safe_int(stats.get('viewCount')),
            'likes': _safe_int(stats.get('likeCount')),
            'published_at': v['snippet']['publishedAt'],
            'subscriber_count': subscriber_count,
        })

    return videos
