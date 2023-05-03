#Youtube Shorts to Instagram

This is a Python script that automatically downloads the latest Youtube short video and uploads it to your Instagram account. The script uses the Youtube Data API and the Instagrapi library to access and authenticate with the two platforms.

##Features

Downloads the latest Youtube short video using the Youtube Data API and the youtube-dl library.

Uploads the video to your Instagram account using the Instagrapi library.

Checks if the video has already been uploaded to your Instagram account to avoid uploading duplicate videos.

Logs the path of each uploaded video to a log file for future reference.

Uses SOLID and DRY code principles to create a modular, maintainable, and extensible codebase.

##Usage

Clone the repository to your local machine.

Install the required libraries by running pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client instagrapi youtube-dl in your terminal or IDE.

Modify the client_secrets.json file with your Youtube API key and the config.json file with your Instagram API key and credentials.

Run the main.py script using python main.py in your terminal or IDE.

Schedule the script to run automatically using a task scheduling system like cron or Task Scheduler.

##License

This script is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you give credit to the original author and include a copy of the license.

##Disclaimer

This script is provided "as is" and without warranty of any kind. The author is not responsible for any damage or loss caused by the use or misuse of this script. Use at your own risk.
