# DeepSeek API Setup Guide

## 1. Environment Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

2. Create `requirements.txt`:
```
openai>=1.12.0  # DeepSeek uses OpenAI-compatible API
python-dotenv>=1.0.1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 2. API Configuration

1. Create `.env` file in your project root:
```
DEEPSEEK_API_KEY=your_api_key_here
```

Note: DeepSeek's recommended base URL is:
- `https://api.deepseek.com/v1` (OpenAI-compatible version)

## 3. Test Script

Create `test_deepseek.py`:

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

def test_deepseek_api():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('DEEPSEEK_API_KEY')
    
    if not api_key:
        print("Error: DEEPSEEK_API_KEY not found in environment variables")
        return
        
    print(f"API Key found: {'Yes' if api_key else 'No'}")
    print(f"API Key length: {len(api_key) if api_key else 'N/A'}")
    
    # Configure OpenAI client for DeepSeek
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com/v1"
    )
    
    try:
        # Test DeepSeek Chat
        print("\nTesting DeepSeek Chat...")
        chat_response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Write a tweet about artificial intelligence"}
            ],
            max_tokens=150,
            temperature=0.7
        )
        print("DeepSeek Response:", chat_response.choices[0].message.content)
        
        print("\nAPI connection successful!")
    except Exception as e:
        print(f"API Test Error: {str(e)}")

if __name__ == "__main__":
    test_deepseek_api()
```

## 4. Run Test

```bash
python test_deepseek.py
```

Expected successful output:
```
API Key found: Yes
API Key length: [Your key length]

Testing DeepSeek Chat...
DeepSeek Response: [Generated tweet about AI]

API connection successful!
```

## 5. Integration Example

Here's how to integrate DeepSeek into your application:

```python
from openai import OpenAI

def initialize_deepseek(api_key):
    return OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com/v1"
    )

def generate_content(client, prompt, system_message="You are a helpful assistant"):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"DeepSeek API error: {str(e)}")
```

## 6. Available Models

1. **DeepSeek Chat**
   - Model name: `deepseek-chat`
   - General-purpose chat model
   - Best for conversation, content generation, and creative tasks
   - Supports system messages and chat-style interactions

## 7. Best Practices

1. **API Key Security**
   - Never hardcode your API key in source code
   - Use environment variables or secure key management
   - Add `.env` to your `.gitignore`

2. **Error Handling**
   - Always implement proper error handling
   - Check for API key presence before making requests
   - Handle API rate limits and timeouts gracefully

3. **Response Processing**
   - Validate response content before using it
   - Implement retry logic for failed requests
   - Consider implementing response caching for frequently used prompts

## 8. Troubleshooting

If you encounter issues:
1. Verify your API key is correctly set in the `.env` file
2. Ensure there are no extra spaces or quotes around the API key
3. Make sure `load_dotenv()` is called before accessing the API key
4. Check that you're using the correct base URL (`https://api.deepseek.com/v1`)
5. Verify your network connection and any proxy settings 