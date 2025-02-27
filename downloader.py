import scrapetube
import requests
import re
from collections import Counter
import yt_dlp


def longer_than_a_minute(info, *, incomplete):
    """Download only videos longer than a minute (or with unknown duration)"""
    duration = info.get('duration')
    if duration and duration < 60:
        return 'The video is too short'

ydl_opts = {
    'match_filter': longer_than_a_minute,
}


"""An error file is available and list all videos that could not be downloaded
"""
def download(urls):
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    with open("errors.txt", "w", encoding="utf-8") as f:
      for idx, vid in enumerate(urls):
        try:
          error_code = ydl.download(vid)
          f.write(f"{error_code} - {vid}\n")
        except Exception as e:
          f.write(f"OTHER ERROR-{e}-{vid}\n")

"""Get YouTube channel ID from a video link.
"""
def get_channel_id(video_url):
    response = requests.get(video_url)
    page_content = response.text

    list_of_re = [
        r'"browseId":"([A-Za-z0-9]+(?:_[A-Za-z0-9]+)+)"',
        r'"channelIds":\["([A-Za-z0-9]+(?:_[A-Za-z0-9]+)+)"\]',
        r'channel/([A-Za-z0-9]+(?:_[A-Za-z0-9]+)+)/'
    ]

    results = []
    for pattern in list_of_re:
        matches = re.findall(pattern, page_content.replace(" ", ""))
        results.extend(matches)
    
    if results:
        most_common = Counter(results).most_common(1)[0]
        return most_common[0]
    return ""


if __name__ == "__main__":
  "enter any video url of the channel"
  video_url = "https://www.youtube.com/watch?v="
  channel_id = get_channel_id(video_url)
  print(channel_id)
  
  videos_ids = scrapetube.get_channel(channel_id)
  
  #  could take a few seconds to list all videos, consider using a for loop with a limit instead
  # urls = [f"https://www.youtube.com/watch?v={video['videoId']}" for video in videos_ids]
  limit = 100
  urls = []
  for idx, vid in enumerate(videos_ids):
    url = f"https://www.youtube.com/watch?v={vid['videoId']}"
    urls.append(url)
    if idx == limit: break
    
  ""
  download(urls)
  
  
  
