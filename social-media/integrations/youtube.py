import os
from googleapiclient.discovery import build

def _get_service():
    """Build YouTube Data API v3 service using API key."""
    return build('youtube', 'v3', developerKey=os.environ['YOUTUBE_API_KEY'])

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
    playlist_id = item['contentDetails']['relatedPlaylists']['uploads']
    subscriber_count = int(item['statistics'].get('subscriberCount', 0))

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
        stats = v['statistics']
        videos.append({
            'video_id': v['id'],
            'title': v['snippet']['title'],
            'url': f"https://youtube.com/watch?v={v['id']}",
            'views': int(stats.get('viewCount', 0)),
            'likes': int(stats.get('likeCount', 0)),
            'published_at': v['snippet']['publishedAt'],
            'subscriber_count': subscriber_count,
        })

    return videos
