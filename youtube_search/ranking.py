from youtube_search.nlp import get_embedding, calculate_similarity


def rank_videos(description, videos):
    """Rank videos based on similarity to the description."""
    description_embedding = get_embedding(description)
    video_scores = []

    for video in videos:
        video_title = video["snippet"]["title"]
        video_description = video["snippet"]["description"]
        video_embedding = get_embedding(video_title + " " + video_description)
        similarity = calculate_similarity(
            description_embedding, video_embedding)
        video_scores.append((video, similarity))

    # Sort videos by similarity score in descending order
    ranked_videos = sorted(video_scores, key=lambda x: x[1], reverse=True)
    return ranked_videos
