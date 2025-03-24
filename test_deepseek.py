import os
from openai import OpenAI
from dotenv import load_dotenv

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
        # Test 1: Simple greeting
        print("\nTest 1: Simple greeting")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Say hello!"}
            ],
            max_tokens=150,
            temperature=0.7
        )
        print("Response:", response.choices[0].message.content)
        
        # Test 2: Generate a tweet
        print("\nTest 2: Tweet generation")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a social media expert who writes engaging tweets."},
                {"role": "user", "content": "Write a tweet about artificial intelligence, including emojis."}
            ],
            max_tokens=150,
            temperature=0.7
        )
        print("Generated tweet:", response.choices[0].message.content)
        print("Tweet length:", len(response.choices[0].message.content))
        
        print("\nAll tests completed successfully!")
        
    except Exception as e:
        print(f"API Test Error: {str(e)}")

if __name__ == "__main__":
    test_deepseek_api() 