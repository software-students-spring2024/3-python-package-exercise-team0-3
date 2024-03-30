![Python build & test](https://github.com/software-students-spring2024/3-python-package-exercise-team0-3/actions/workflows/build.yaml/badge.svg)

# GPT Coder

## Description 
This package is designed to help users write better and more fun code. It allows users to modify the conciseness, commenting, and readability of the code returned
by the GPT model. Through the usage of this package, users can expect code responses that are more tailored towards their preferences.

## Instructions

Ensure that you already have pipenv installed. If not, you can install it by running the following command:
```bash
pip install pipenv
```

In order to use our package, run this line in your terminal:
```bash
pip install gptcoder
```

Then, add this line to the top of your file:
```python
from gptcoder import GPTCoder
```

# Functions

1. set_language
    - Description: This function sets the language of the code to be generated.
    - Parameters: 
      - language_code: int
        - Description: The code corresponding to the programming language of the code to be generated.
        - Values: 1. Python, 2. JavaScript, 3. Java, 4. C, 5. C++, 6. C#, 7. TypeScript, 8. PHP, 9. Swift, 10. Ruby
        - Default: 1

2. set_conciseness
    - Description: This function sets the conciseness of the code to be generated.
    - Parameters: 
      - conciseness: int
        - Description: The conciseness of the code to be generated.
        - Values: 1-10
        - Default: 1
  
3. set_commenting
    - Description: This function sets the commenting of the code to be generated.
    - Parameters: 
      - commenting: int
        - Description: The commenting of the code to be generated.
        - Values: 1-10
        - Default: 5

4. set_readability
    - Description: This function sets the readability of the code to be generated.
    - Parameters: 
      - readability: int
        - Description: The readability of the code to be generated.
        - Values: 1-10
        - Default: 10
  
5. generate_code
    - Description: This function generates code based on the given prompt.
    - Parameters: 
      - code_prompt: str
        - Description: The prompt for the code to be generated.
        - Values: Any string
        - Default: None

## Team Members

## Package Page
- link to Package in PyPi
