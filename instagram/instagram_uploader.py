# instagram/instagram_uploader.py

import glob

from instagram.instagram_api import InstagramAPI
from youtube.youtube_downloader import YoutubeDownloader


class InstagramUploader:
    def __init__(self, input_dir='videos'):
        self.input_dir = input_dir
        self.instagram_api = InstagramAPI()

    def upload_latest_video_to_instagram(self):
    video_files = glob.glob(f'{self.input_dir}/*.mp4')
    if video_files:
        latest_video_file = max(video_files, key=os.path.getctime)
        uploaded_media = self.instagram_api.client.feed_timeline().get()["items"]

        # check if latest video has already been uploaded
        for media in uploaded_media:
            if 'video_versions' in media and media['video_versions'][0]['url'] == latest_video_file:
                print('Latest video has already been uploaded.')
                return

        # upload the latest video to Instagram
        self.instagram_api.upload_video(latest_video_file)
        os.remove(latest_video_file)  # delete the video file

        # add a log entry for the uploaded video
        with open('log.txt', 'a') as f:
            f.write(f'{latest_video_file}\n')

    else:
        print('No videos found in directory.')

    def download_latest_short_video(self):
        youtube_downloader = YoutubeDownloader(output_dir=self.input_dir)
        youtube_downloader.download_latest_short_video()
