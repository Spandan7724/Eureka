import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
CACHE_PATH = "data/cache/"
DATABASE_PATH = "data/videos.db"
