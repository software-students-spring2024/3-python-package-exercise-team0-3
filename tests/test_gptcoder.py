import pytest
from gptcoder import gptcoder
from unittest.mock import patch
from dotenv import load_dotenv
import os

load_dotenv()

# Load the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# TODO: ADD UNIT TESTS
class Tests:
    
    @pytest.fixture
    def fixture(self):
        pass

    def test_sanity_check(self, fixture):
        pass

    class Test_get_language:

        @pytest.mark.parametrize("input_value", [("2")])
        def test_output(self, input_value):
            # mocks user input
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_language()
                assert output is not None, "Expected get_language() to return output. Instead, it returned None"
        
        @pytest.mark.parametrize("input_value", [("2")])
        def test_is_string(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_language()
                assert isinstance(
                output, str
            ), f"Expected get_language() to return a string. Instead, it returned {output}"

        @pytest.mark.parametrize("input_value", [("2")])
        def test_is_language(self, input_value):
            with patch('builtins.input', return_value=input_value):
                language_dict = ["Python", "JavaScript", "Java", "C", 
                   "C++", "C#", "TypeScript", "PHP", "Swift", "Ruby"]
                output = gptcoder.get_language()
                assert output in language_dict, f"Expected get_language() to return a programming language. Instead, it returned {output}"
    
    class Test_get_conciseness:

        @pytest.mark.parametrize("input_value", [(2)])
        def test_output(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_conciseness()
                assert output is not None, "Expected get_conciseness() to return output. Instead, it returned None"
        
        @pytest.mark.parametrize("input_value", [(2)])
        def test_is_int(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_conciseness()
                assert isinstance(
                output, int
            ), f"Expected get_conciseness() to return an int. Instead, it returned {output}"

        @pytest.mark.parametrize("input_value", [(2)])
        def test_is_in_range(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_conciseness()
                assert(1 <= output <= 10), f"Expected get_conciseness() to return an int between 10 and 100. Instead, it returned {output}"
    
    class Test_get_commenting:

        @pytest.mark.parametrize("input_value", [(2)])
        def test_output(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_commenting()
                assert output is not None, "Expected get_commenting() to return output. Instead, it returned None"
        
        @pytest.mark.parametrize("input_value", [(2)])
        def test_is_int(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_commenting()
                assert isinstance(
                output, int
            ), f"Expected get_commenting() to return an int. Instead, it returned {output}"

        @pytest.mark.parametrize("input_value", [(2)])
        def test_is_in_range(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_commenting()
                assert(1 <= output <= 10), f"Expected get_commenting() to return an int between 10 and 100. Instead, it returned {output}"

    class Test_get_readability:

        @pytest.mark.parametrize("input_value", [(2)])
        def test_output(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_readability()
                assert output is not None, "Expected get_readability() to return output. Instead, it returned None"
        
        @pytest.mark.parametrize("input_value", [(2)])
        def test_is_int(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_readability()
                assert isinstance(
                output, int
            ), f"Expected get_readability() to return an int. Instead, it returned {output}"

        @pytest.mark.parametrize("input_value", [(2)])
        def test_is_in_range(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_readability()
                assert(1 <= output <= 10), f"Expected get_readability() to return an int between 10 and 100. Instead, it returned {output}"

    class Test_prompt_user:

        @pytest.mark.parametrize("input_value", [("2")])
        def test_output(self, input_value):
            # mocks user input
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.prompt_user()
                assert output is not None, "Expected prompt_user() to return output. Instead, it returned None"
        
        @pytest.mark.parametrize("input_value", [("2")])
        def test_is_string(self, input_value):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.prompt_user()
                assert isinstance(
                output, str
            ), f"Expected prompt_user() to return a string. Instead, it returned {output}"

        # TODO: Add third test that tests if string is a prompt
                
    class Test_callAPI:

        def test_output(self):
            output = gptcoder.callAPI(api_key)
            assert output.object=="chat.completion", f"Expected callAPI() to return a chat completion object. Instead, it returned {output}"
        
        # TODO: Add 2nd test testing if message is cod

        # TODO: Add 3rd test that tests if languge is correct
        
        
        
        


