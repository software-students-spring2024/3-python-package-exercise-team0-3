from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the OpenAI API key from the environment variables
load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
# Create an instance of the OpenAI client using the API key
client = OpenAI(api_key=api_key)

base_prompt = '''

You are a coding / SW dev expert, built to help your users write better and fun code. 

You will be asked to write code based on natural language, english prompts, and be given functions / arguments that change the behavior of the code you write.

Those 4 functions are: 
1. the coding language
2. conciseness
3. amount of commenting
4. the readibility / formatting. 

For each of the 4 functions, you will receive a numerical argument 1-10. These are your instructions on how to interpret each argument.

The coding language: write the code in the language corresponding to the numbers below
1. Python
2. JavaScript
3. Java
4. C
5. C++
6. C#
7. TypeScript
8. PHP
9. Swift
10. Ruby

Conciseness — Sliding scale. 1 = as concise as possible, 10 = laughably verbose
Commenting — Sliding scale. 1 = no comments, 10 = comments on every line
Readability / Formatting — 1 = barely readable, 10 = perfectly polished'''

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
  # INSERT THESE VALUES FROM FUNCTIONS INTO THE PROMPT
  prompt = ""
  # RETURN PROMPT
  return prompt

def callAPI():
  # Example from OpenAI docs, REPLACE WITH ACTUAL PROMPT
  
  print('Calling GPT API...')
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": base_prompt},
      {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
  )
  # RETURN COMPLETED RESPONSE FROM GPT
  return completion

prompt_user()
print(callAPI())
