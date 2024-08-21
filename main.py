import click
from youtube_search.search import search_videos
from youtube_search.ranking import rank_videos
from youtube_search.utils import display_results


@click.command()
@click.argument("description")
@click.option("--num_results", default=10, help="Number of video results to display.")
def search(description, num_results):
    """Search YouTube videos based on the description provided by the user."""
    videos = search_videos(description)
    ranked_videos = rank_videos(description, videos)
    display_results(ranked_videos[:num_results])


if __name__ == "__main__":
    search()
