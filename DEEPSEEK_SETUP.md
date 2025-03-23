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
python-dotenv==0.21.1
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

Note: DeepSeek supports two base URLs:
- `https://api.deepseek.com`
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
        base_url="https://api.deepseek.com"  # or https://api.deepseek.com/v1
    )
    
    try:
        # Test DeepSeek-V3 (deepseek-chat)
        print("\nTesting DeepSeek-V3...")
        chat_response = client.chat.completions.create(
            model="deepseek-chat",  # This uses DeepSeek-V3
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Hello"}
            ],
            stream=False
        )
        print("DeepSeek-V3 Response:", chat_response.choices[0].message.content)
        
        # Test DeepSeek-R1 (deepseek-reasoner)
        print("\nTesting DeepSeek-R1...")
        reasoner_response = client.chat.completions.create(
            model="deepseek-reasoner",  # This uses DeepSeek-R1
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Solve this problem: If a train travels at 60 mph, how long will it take to cover 180 miles?"}
            ],
            stream=False
        )
        print("DeepSeek-R1 Response:", reasoner_response.choices[0].message.content)
        
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

Testing DeepSeek-V3...
DeepSeek-V3 Response: [Response from DeepSeek-V3]

Testing DeepSeek-R1...
DeepSeek-R1 Response: [Response from DeepSeek-R1]

API connection successful!
```

## 5. Available Models

1. **DeepSeek-V3** (General Chat Model)
   - Model name: `deepseek-chat`
   - Latest version of the chat model
   - Best for general conversation and tasks

2. **DeepSeek-R1** (Reasoning Model)
   - Model name: `deepseek-reasoner`
   - Specialized for reasoning tasks
   - Best for problem-solving and logical analysis

## 6. Troubleshooting

If you get an authentication error:
1. Verify your API key is correctly copied in the `.env` file
2. Ensure there are no extra spaces or quotes around the API key
3. Make sure `load_dotenv()` is called before accessing the API key
4. Try both base URLs (`https://api.deepseek.com` and `https://api.deepseek.com/v1`) 