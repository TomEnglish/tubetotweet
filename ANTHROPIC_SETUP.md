# Anthropic API Setup Guide

## 1. Environment Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

2. Create `requirements.txt`:
```
anthropic==0.18.1
python-dotenv==0.21.1
```

3. Install dependencies:
```bash
# On macOS, if tokenizers installation fails, first run:
pip install --no-build-isolation tokenizers==0.13.3

# Then install remaining dependencies:
pip install -r requirements.txt
```

## 2. API Configuration

1. Create `.env` file in your project root:
```
CLAUDE_API_KEY=your_api_key_here
```

2. Add to `.gitignore`:
```
.env
```

## 3. Test Script

Create `test_claude.py`:

```python
import os
import anthropic
from dotenv import load_dotenv

def test_claude_api():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('CLAUDE_API_KEY')
    
    if not api_key:
        print("Error: CLAUDE_API_KEY not found in environment variables")
        return
        
    print(f"API Key found: {'Yes' if api_key else 'No'}")
    print(f"API Key length: {len(api_key) if api_key else 'N/A'}")
    
    # Initialize the client with explicit API key
    client = anthropic.Anthropic(
        api_key=api_key
    )
    
    # Test data
    test_video = {
        'title': 'Test Video Title',
        'description': 'This is a test video description',
        'url': 'https://youtube.com/test'
    }
    
    prompt = f"""Generate an engaging tweet (max 280 characters) for this YouTube video:
Title: {test_video['title']}
Description: {test_video['description']}
Make it catchy and include the video URL at the end."""

    try:
        print("\nTesting Claude API connection...")
        message = client.messages.create(
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
        
        print("\nAPI Response:")
        print(message.content)
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_claude_api()
```

## 4. Run Test

```bash
python test_claude.py
```

Expected successful output:
```
API Key found: Yes
API Key length: 108

Testing Claude API connection...

API Response:
[ContentBlock(text='Unlock the secrets of video mastery! 🎥 Dive into "Test Video Title" and discover game-changing insights. Don't miss this captivating exploration! 👀\n\nhttps://youtu.be/[VIDEO_URL]', type='text')]
```

## 5. Troubleshooting

If you get an authentication error:
1. Verify your API key is correctly copied in the `.env` file
2. Ensure there are no extra spaces or quotes around the API key
3. Make sure `load_dotenv()` is called before accessing the API key

Common installation issues:
1. If you encounter issues installing `tokenizers` on macOS:
   - Use the pre-built wheel: `pip install --no-build-isolation tokenizers==0.13.3`
   - Then install the remaining requirements
2. If you see "Could not resolve authentication method" error:
   - Make sure your API key is properly set in the `.env` file
   - Verify that the API key is being loaded correctly in the environment 