from openai import OpenAI

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

class GPTCoder:
  
  def __init__(self, api_key, language=1, conciseness=1, commenting=5, readability=10):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        self.language = self.get_language_name(language)
        self.conciseness = conciseness
        self.commenting = commenting
        self.readability = readability

  # Get programming language static method
  @staticmethod
  def get_language_name(language_code):
      language_dict = {
          1: "Python", 2: "JavaScript", 3: "Java", 4: "C",
          5: "C++", 6: "C#", 7: "TypeScript", 8: "PHP", 9: "Swift", 10: "Ruby"
      }
      return language_dict.get(language_code, "Python")
        
  def set_language(self, language_code):
    if isinstance(language_code, int):
      self.language = self.get_language_name(language_code)
    else:
      raise ValueError("ERROR: Argument must be an integer")

  def set_conciseness(self, conciseness):
    if isinstance(conciseness, int):
      self.conciseness = conciseness
    else:
      raise ValueError("ERROR: Argument must be an integer")

  def set_commenting(self, commenting):
    if isinstance(commenting, int):
      self.commenting = commenting
    else:
      raise ValueError("ERROR: Argument must be an integer")

  def set_readability(self, readability):
    if isinstance(readability, int):
      self.readability = readability
    else:
      raise ValueError("ERROR: Argument must be an integer")

  def generate_code(self, code_prompt):

    prompt = f"{code_prompt} Language: {self.language} Conciseness: {self.conciseness} Commenting: {self.commenting} Readability: {self.readability}"

    print('Calling GPT API...')
    completion = self.client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": base_prompt},
        {"role": "user", "content": prompt}
      ]
    )

    generated_code = completion.choices[0].message.content
    
    return generated_code
    

