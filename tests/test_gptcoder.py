import pytest
from gptcoder import GPTCoder
from unittest.mock import patch, MagicMock

class Tests:

    api_key = "mock_api_key"
    
    def test_sanity_check():
        expected = True
        actual = True
        assert actual == expected

    # Test the constructor and attribute setting
    def test_init(self):
        coder = GPTCoder(self.api_key, 2, 3, 4, 5)
        assert coder.api_key == self.api_key
        assert coder.language == "JavaScript"
        assert coder.conciseness == 3
        assert coder.commenting == 4
        assert coder.readability == 5

    # Test get_language_name static method
    @pytest.mark.parametrize("code, expected", [
        (1, "Python"),
        (5, "C++"),
        (10, "Ruby"),
        (99, "Python")  # Default case
    ])
    def test_get_language_name(self, code, expected):
        assert GPTCoder.get_language_name(code) == expected

    # Mock the OpenAI API call for generate_code
    @patch('gptcoder.GPTCoder.OpenAI')
    def test_generate_code(self, mock_openai):
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content='Generated Code'))]
        mock_openai.return_value.chat.completions.create.return_value = mock_response

        coder = GPTCoder(self.api_key)
        result = coder.generate_code("Create a Python function to add two numbers")
        
        assert result == "Generated Code"
        mock_openai.return_value.chat.completions.create.assert_called_once()

    @patch('gptcoder.GPTCoder.OpenAI')  # Mock the OpenAI class
    def test_initialization_with_mock_api_key(self, mock_openai):
        coder = GPTCoder(api_key='mock_api_key')
        assert coder.api_key == 'mock_api_key', "API key should be correctly stored"

    def test_set_language(self, coder, language_code, expected_language):
        coder.set_language(language_code)
        assert coder.language == expected_language, f"Expected language to be set to {expected_language}"

    # Test setting conciseness
    @pytest.mark.parametrize("conciseness", [1, 5, 10])
    def test_set_conciseness(self, coder, conciseness):
        coder.set_conciseness(conciseness)
        assert coder.conciseness == conciseness, f"Expected conciseness to be set to {conciseness}"

    # Test setting commenting
    @pytest.mark.parametrize("commenting", [1, 5, 10])
    def test_set_commenting(self, coder, commenting):
        coder.set_commenting(commenting)
        assert coder.commenting == commenting, f"Expected commenting to be set to {commenting}"

    # Test setting readability
    @pytest.mark.parametrize("readability", [1, 5, 10])
    def test_set_readability(self, coder, readability):
        coder.set_readability(readability)
        assert coder.readability == readability, f"Expected readability to be set to {readability}"

'''
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
'''
