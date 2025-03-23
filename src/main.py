import os
import anthropic
import openai
from dotenv import load_dotenv
import feedparser
import argparse
import requests

class YouTubeVideoFetcher:
    def __init__(self, channel_id=None):
        self.channel_id = channel_id or os.getenv('YOUTUBE_CHANNEL_ID')
        if not self.channel_id:
            raise ValueError("YouTube channel ID not provided. Use --channel-id argument or set YOUTUBE_CHANNEL_ID in .env")
        self.rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={self.channel_id}"
        self.channel_title = self._get_channel_title()

    def _get_channel_title(self) -> str:
        """Fetch the channel title from the RSS feed."""
        try:
            feed = feedparser.parse(self.rss_url)
            if feed.feed and hasattr(feed.feed, 'title'):
                return feed.feed.title
            return "Unknown Channel"
        except Exception as e:
            return "Unknown Channel"

    def get_recent_videos(self, max_results: int = 3) -> list:
        feed = feedparser.parse(self.rss_url)
        videos = []
        
        for entry in feed.entries[:max_results]:
            video = {
                'title': entry.title,
                'description': entry.description,
                'video_id': entry.yt_videoid,
                'url': entry.link
            }
            videos.append(video)
        return videos

class TweetGenerator:
    MAX_TWEET_LENGTH = 280

    def __init__(self, provider='claude'):
        self.provider = provider.lower()
        
        if self.provider == 'claude':
            api_key = os.getenv('CLAUDE_API_KEY')
            if not api_key:
                raise ValueError("CLAUDE_API_KEY not found in environment variables")
            self.client = anthropic.Anthropic(api_key=api_key)
        
        elif self.provider == 'deepseek':
            api_key = os.getenv('DEEPSEEK_API_KEY')
            if not api_key:
                raise ValueError("DEEPSEEK_API_KEY not found in environment variables")
            openai.api_key = api_key
            openai.api_base = "https://api.deepseek.com/beta"
            self.client = openai
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def enforce_character_limit(self, tweet: str) -> str:
        """Enforce the character limit on a tweet."""
        if len(tweet) <= self.MAX_TWEET_LENGTH:
            return tweet
            
        # If over limit, try to find a natural breakpoint
        breakpoints = ['\n\n', '\n', '. ', '! ', '? ', ' ']
        tweet_without_url = tweet
        url = None
        
        # Extract URL if present
        import re
        url_match = re.search(r'https?://\S+', tweet)
        if url_match:
            url = url_match.group()
            tweet_without_url = tweet.replace(url, '').strip()
        
        # Try different breakpoints
        for breakpoint in breakpoints:
            if breakpoint in tweet_without_url:
                parts = tweet_without_url.split(breakpoint)
                truncated = parts[0].strip()
                
                # Add back URL if it exists
                if url:
                    if len(truncated) + len(url) + 4 <= self.MAX_TWEET_LENGTH:  # +4 for space and ellipsis
                        return f"{truncated}... {url}"
                    else:
                        return f"{truncated[:self.MAX_TWEET_LENGTH - len(url) - 4]}... {url}"
                else:
                    if len(truncated) + 3 <= self.MAX_TWEET_LENGTH:  # +3 for ellipsis
                        return f"{truncated}..."
                    else:
                        return f"{truncated[:self.MAX_TWEET_LENGTH - 3]}..."
        
        # If no good breakpoint found, just truncate
        if url:
            return f"{tweet_without_url[:self.MAX_TWEET_LENGTH - len(url) - 4]}... {url}"
        return f"{tweet[:self.MAX_TWEET_LENGTH - 3]}..."

    def generate_tweet(self, video: dict) -> str:
        prompt = f"""Generate a concise, engaging tweet (STRICTLY under {self.MAX_TWEET_LENGTH} characters) for this YouTube video:
Title: {video['title']}
Description: {video['description']}

Requirements:
1. MUST be under {self.MAX_TWEET_LENGTH} characters
2. Include emojis for engagement
3. Make it catchy and compelling
4. Include the video URL: {video['url']}
5. NO hashtags unless there's room
6. NO line breaks unless necessary"""

        try:
            if self.provider == 'claude':
                message = self.client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=150,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": prompt
                                }
                            ]
                        }
                    ]
                )
                tweet = message.content[0].text
            
            else:  # deepseek
                response = self.client.Completion.create(
                    model="deepseek-chat",
                    prompt=f"System: You are a social media expert who writes engaging tweets that are always under 280 characters.\n\nUser: {prompt}",
                    max_tokens=150,
                    temperature=0.7,
                    stop=None
                )
                tweet = response.choices[0].text.strip()
            
            # Enforce character limit
            return self.enforce_character_limit(tweet)
                
        except Exception as e:
            raise Exception(f"{self.provider.capitalize()} API error: {str(e)}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate tweets for recent YouTube videos')
    parser.add_argument('--channel-id', type=str, help='YouTube channel ID to fetch videos from')
    parser.add_argument('--provider', type=str, choices=['claude', 'deepseek'], 
                       help='AI provider to use (claude or deepseek)')
    parser.add_argument('--max-videos', type=int, default=3,
                       help='Maximum number of recent videos to process (default: 3)')
    args = parser.parse_args()

    # Load environment variables
    load_dotenv()
    
    # Get provider choice (command line arg takes precedence over env var)
    provider = args.provider or os.getenv('AI_PROVIDER', 'claude').lower()
    print(f"Using AI Provider: {provider.capitalize()}")
    
    try:
        # Initialize components
        youtube_fetcher = YouTubeVideoFetcher(args.channel_id)
        tweet_generator = TweetGenerator(provider)

        # Display channel information
        print(f"\nConnected to YouTube Channel: {youtube_fetcher.channel_title}")
        print(f"Channel ID: {youtube_fetcher.channel_id}")

        # Get recent videos
        print("\nFetching recent YouTube videos...")
        videos = youtube_fetcher.get_recent_videos(args.max_videos)
        
        if not videos:
            print(f"No videos found for channel: {youtube_fetcher.channel_title} (ID: {youtube_fetcher.channel_id})")
            return

        # Generate tweets for each video
        print("\n=== Generated Tweets ===\n")
        for i, video in enumerate(videos, 1):
            print(f"Tweet #{i} for video: {video['title']}")
            tweet_content = tweet_generator.generate_tweet(video)
            print("\nTweet content:")
            print("=" * 50)
            print(tweet_content)
            print("=" * 50)
            print(f"Character count: {len(tweet_content)}\n")
            
        print("\nAll tweets generated successfully!")

    except ValueError as ve:
        print(f"Configuration error: {str(ve)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 