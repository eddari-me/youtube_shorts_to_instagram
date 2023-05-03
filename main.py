
# main.py

from youtube.youtube_api import YoutubeAPI
from instagram.instagram_uploader import InstagramUploader


def main():
    youtube_api = YoutubeAPI()
    instagram_uploader = InstagramUploader()

    youtube_api.authenticate()
    instagram_uploader.instagram_api.authenticate()

    instagram_uploader.download_latest_short_video()
    instagram_uploader.upload_latest_video_to_instagram()


if __name__ == '__main__':
    main()

