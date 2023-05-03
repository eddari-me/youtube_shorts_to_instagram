# youtube/youtube_api.py

import google.auth
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config.config import YOUTUBE_API_KEY


class YoutubeAPI:
    def __init__(self):
        self.credentials = None
        self.client = None

    def authenticate(self):
        self.credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/youtube.readonly'])
        self.client = build('youtube', 'v3', credentials=self.credentials)

    def get_latest_short_videos(self, max_results=10):
        if not self.client:
            self.authenticate()

        request = self.client.search().list(
            part='id,snippet',
            q='#shorts',
            type='video',
            maxResults=max_results,
            order='date'
        )

        response = request.execute()
        videos = response['items']
        video_ids = [video['id']['videoId'] for video in videos]
        video_urls = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids]

        return video_urls
