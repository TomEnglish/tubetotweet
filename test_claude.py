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