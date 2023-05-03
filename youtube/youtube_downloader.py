# youtube/youtube_downloader.py

import os
import subprocess
import requests

from config.config import YOUTUBE_API_KEY


class YoutubeDownloader:
    def __init__(self, output_dir='videos'):
        self.output_dir = output_dir

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def download_latest_short_video(self):
        video_url = self.get_latest_short_video_url()
        video_file = os.path.join(self.output_dir, f'{video_url.split("=")[-1]}.mp4')
        self.download_video(video_url, video_file)

    def get_latest_short_video_url(self):
        response = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC-lHJZR3Gqxm24_Vd_AJ5Yw&maxResults=1&order=date&key={YOUTUBE_API_KEY}&q=%23shorts&type=video')
        response.raise_for_status()
        video_id = response.json()['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        return video_url

    def download_video(self, url, output_file):
        command = f'youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 {url} -o {output_file}'
        subprocess.call(command, shell=True)
