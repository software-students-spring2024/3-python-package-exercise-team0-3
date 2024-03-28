from gptcoder import GPTCoder
from dotenv import load_dotenv
import os

load_dotenv(override=True)

def main():
    # User provides their OpenAI API key.
    api_key = os.getenv("OPENAI_API_KEY")

    # Initialize the GPTCoder client with the user's API key.
    coder = GPTCoder(api_key)

    # The user could also confqgure the language and other parameters if needed.
    coder.set_language(1)  # 1 corresponds to Python.
    coder.set_conciseness(5)  # Moderate level of conciseness.
    coder.set_commenting(10)  # High level of commenting for clarity.
    coder.set_readability(10)  # Maximize readability.

    # Prompt the user to enter the code generation prompt.
    prompt = input("Enter the code generation prompt: ")

    # Now, call the generate_code method with the user's prompt.
    code_generation_response = coder.generate_code(prompt)

    # Assuming the response includes the generated code directly,
    # print or process the generated code.
    print("Generated Code:\n", code_generation_response)

if __name__ == "__main__":
    main()