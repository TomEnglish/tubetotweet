# TubeToTweet 🎥 ➡️ 🐦

An AI-powered tool that generates engaging tweets from YouTube videos. Supports multiple AI providers (Claude and DeepSeek) for tweet generation.

## Features

- Fetch recent videos from any YouTube channel
- Generate engaging tweets using AI (Claude or DeepSeek)
- Automatic character limit enforcement for tweets
- Support for emojis and hashtags
- Command-line interface for easy use
- Environment variable configuration

## Prerequisites

- Python 3.7+
- YouTube Channel ID
- API key for either Claude or DeepSeek

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tubetotweet.git
cd tubetotweet
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
# On macOS, if tokenizers installation fails, first run:
pip install --no-build-isolation tokenizers==0.13.3

# Then install remaining dependencies:
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```
CLAUDE_API_KEY=your_claude_api_key_here
DEEPSEEK_API_KEY=your_deepseek_api_key_here
YOUTUBE_CHANNEL_ID=default_channel_id_here  # Optional
```

## Usage

Basic usage:
```bash
python main.py --channel-id=CHANNEL_ID
```

Options:
- `--channel-id`: YouTube channel ID to fetch videos from
- `--provider`: AI provider to use (`claude` or `deepseek`, defaults to claude)
- `--max-videos`: Maximum number of recent videos to process (default: 3)

Examples:
```bash
# Use Claude (default) with specific channel
python main.py --channel-id=UCsBjURrPoezykLs9EqgamOA

# Use DeepSeek and process 5 videos
python main.py --channel-id=UCsBjURrPoezykLs9EqgamOA --provider=deepseek --max-videos=5
```

## Configuration

The application can be configured using either command-line arguments or environment variables:

1. Command-line arguments take precedence over environment variables
2. Environment variables in `.env` file:
   - `CLAUDE_API_KEY`: Your Claude API key
   - `DEEPSEEK_API_KEY`: Your DeepSeek API key
   - `YOUTUBE_CHANNEL_ID`: Default YouTube channel ID
   - `AI_PROVIDER`: Default AI provider (`claude` or `deepseek`)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 