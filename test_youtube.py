from main import YouTubeVideoFetcher
import json

def test_youtube_fetcher():
    fetcher = YouTubeVideoFetcher()
    print("YouTube Channel ID:", fetcher.channel_id)
    print("\nFetching videos...")
    try:
        videos = fetcher.get_recent_videos()
        print("\nFetched Videos:")
        print(json.dumps(videos, indent=2))
        print(f"\nNumber of videos fetched: {len(videos)}")
    except Exception as e:
        print(f"Error fetching videos: {str(e)}")

if __name__ == "__main__":
    test_youtube_fetcher() 