import requests
from youtube_search.nlp import preprocess_description
from youtube_search.utils import cache_results
from config import YOUTUBE_API_KEY

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"


def search_videos(description):
    """Search YouTube for videos matching the description."""
    query = preprocess_description(description)
    response = requests.get(
        YOUTUBE_SEARCH_URL,
        params={
            "part": "snippet",
            "q": query,
            "key": YOUTUBE_API_KEY,
            "type": "video",
            "maxResults": 25
        }
    )
    if response.status_code == 200:
        videos = response.json().get("items", [])
        cache_results(videos)
        return videos
    else:
        response.raise_for_status()
