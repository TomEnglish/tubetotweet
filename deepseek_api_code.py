# Example code for using the DeepSeek API with the OpenAI SDK
# Install required packages: pip install openai python-dotenv

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv('DEEPSEEK_API_KEY')

if not api_key:
    raise ValueError("DEEPSEEK_API_KEY not found in environment variables")

# Initialize the client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com/v1"
)

# Example: Generate a tweet about AI
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a social media expert who writes engaging tweets."},
        {"role": "user", "content": "Write a tweet about artificial intelligence, including emojis."}
    ],
    max_tokens=150,
    temperature=0.7
)

# Print the generated tweet
print("Generated Tweet:")
print(response.choices[0].message.content)

# Example: Generate a code explanation
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful programming assistant."},
        {"role": "user", "content": "Explain how to use the DeepSeek API in Python."}
    ],
    max_tokens=150,
    temperature=0.7
)

print("\nAPI Usage Explanation:")
print(response.choices[0].message.content)
