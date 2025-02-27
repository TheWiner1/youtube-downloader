# YouTube Video Downloader

This project allows you to download videos from a YouTube channel using `yt_dlp` and `scrapetube`. It extracts the channel ID from a video URL, retrieves video links, and downloads them while filtering out short videos.

## Features
- Extracts channel ID from a YouTube video URL
- Retrieves all video URLs from a channel
- Downloads videos longer than one minute
- Logs errors to an `errors.txt` file

## Installation
```sh
# Clone the repository
git clone https://github.com/TheWiner1/youtube-downloader
cd youtube-downloader

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
```sh
python downloader.py
```
Modify `video_url` in `downloader.py` to the YouTube video URL of a channel you want to scrape.

## Requirements
- Python 3.x
- `yt_dlp`
- `scrapetube`
- `requests`

## Notes
- The script may take some time to list all videos. Consider setting a limit in the loop.
- Error logs for failed downloads are stored in `errors.txt`.
- Also, you could be blacklisted with you perform too many requests


## License
This project is licensed under the MIT License.

