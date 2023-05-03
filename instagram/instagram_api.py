# instagram/instagram_api.py

import os
from instagrapi import Client

from config.config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, INSTAGRAM_API_KEY


class InstagramAPI:
    def __init__(self):
        self.client = None

    def authenticate(self):
        self.client = Client()
        self.client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

    def upload_video(self, video_path):
        if not self.client:
            self.authenticate()

        self.client.upload_video(video_path, thumbnail=None)
