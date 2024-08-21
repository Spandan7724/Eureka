import json
import os
from config import CACHE_PATH
from rich.console import Console
from rich.text import Text

console = Console()

def cache_results(videos):
    """Cache video search results."""
    os.makedirs(CACHE_PATH, exist_ok=True)
    with open(os.path.join(CACHE_PATH, "latest_search.json"), "w") as f:
        json.dump(videos, f)


def display_results(videos):
    for video, similarity in videos:
        title = video["snippet"]["title"]
        description = video["snippet"]["description"]
        url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
        similarity_percentage = similarity * 100

        title_text = Text(f"Title: {title}", style="blue1")
        description_text = Text(f"Description: {description}", style="bright_white")
        url_text = Text(f"URL: {url}", style="underline dark_cyan")
        similarity_text = Text(f"Similarity: {similarity_percentage:.2f}%", style="blue_violet")

        console.print(title_text)
        console.print(description_text)
        console.print(url_text)
        console.print(similarity_text)
        console.print("\n")
