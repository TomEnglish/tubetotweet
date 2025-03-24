from flask import Flask, request, jsonify
from flask_cors import CORS
from main import YouTubeVideoFetcher, TweetGenerator
import os

app = Flask(__name__)
CORS(app)

@app.route('/generate-tweets', methods=['POST'])
def generate_tweets():
    try:
        data = request.json
        channel_id = data.get('channelId')
        provider = data.get('provider', 'claude')
        api_key = data.get('apiKey')
        
        # Set the API key in environment
        if provider == 'claude':
            os.environ['CLAUDE_API_KEY'] = api_key
        else:
            os.environ['DEEPSEEK_API_KEY'] = api_key
            
        # Initialize components
        youtube_fetcher = YouTubeVideoFetcher(channel_id)
        tweet_generator = TweetGenerator(provider)
        
        # Get recent videos and generate tweets
        videos = youtube_fetcher.get_recent_videos(3)
        tweets = []
        
        for video in videos:
            tweet_content = tweet_generator.generate_tweet(video)
            tweets.append({
                'title': video['title'],
                'content': tweet_content,
                'url': video['url']
            })
            
        return jsonify({'tweets': tweets})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 