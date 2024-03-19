from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Load the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Create an instance of the OpenAI client using the API key
client = OpenAI(api_key=api_key)

# example from OPEN AI docs
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)