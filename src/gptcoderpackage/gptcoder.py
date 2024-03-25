from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the OpenAI API key from the environment variables
load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
# Create an instance of the OpenAI client using the API key
client = OpenAI(api_key=api_key)

# Programming language specifier
def get_language():
  # prompt user for programming language
  language = input("Enter the programming language of the code (press ENTER for default [python]): ")
  
  if not language:
    language = "python"
  
  return language

# Conciseness (as concise as possible, all the way to laughably "extra")
def get_conciseness():
  # prompt user for conciseness
  while True:
    conciseness = input("Enter the conciseness of the code [1-10] (press ENTER for default [1]): ")
    
    if not conciseness:
      conciseness = 1
      break
    
    try:
      conciseness = int(conciseness)
      if 1 <= conciseness <= 10:
        break
      else:
        print("Conciseness level should be between 1 and 10.")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 10.")
  
  return conciseness

# Commenting level (from no comments at all to comments on every line)
def get_commenting():
  # prompt user for commenting level
  while True:
    commenting = input("Enter the commenting level of the code [1-10] (press ENTER for default [5]): ")
    
    if not commenting:
      commenting = 5
      break
    
    try:
      commenting = int(commenting)
      if 1 <= commenting <= 10:
        break
      else:
        print("Commenting level should be between 1 and 10.")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 10.")
  
  return commenting

# readability (naming conventions, formatting, etc.) from "barely readable" to "perfectly polished"
def get_readability():
  # prompt user for readability
  while True:
    readability = input("Enter the readability of the code [1-10] (press ENTER for default [10]): ")
    
    if not readability:
      readability = 10
      break
    
    try:
      readability = int(readability)
      if 1 <= readability <= 10:
        break
      else:
        print("Readability level should be between 1 and 10.")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 10.")
  
  return readability

# TODO: prompt user for what code they want to generate and the paramters
def prompt_user():
  code = input("Enter the code you want GPT to generate: ")
  language = get_language()
  conciseness = get_conciseness()
  commenting = get_commenting()
  readability = get_readability()
  # RETURN PROMPT
  return None

def callAPI():
  # Example from OpenAI docs
  print('Calling GPT API...')
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
      {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
  )
  # RETURN COMPLETED RESPONSE FROM GPT
  return completion

prompt_user()
print(callAPI())
