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