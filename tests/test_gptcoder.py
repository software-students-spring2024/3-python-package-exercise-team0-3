import pytest
from gptcoder import gptcoder
from unittest.mock import patch

# TODO: ADD UNIT TESTS
class Tests:
    
    @pytest.fixture
    def fixture(self):
        pass

    def test_sanity_check(self, fixture):
        pass

    class Test_get_language:

        @pytest.mark.parametrize("input_value,expected_output", [
        (2, "JavaScript")])
        def test_output(self, input_value, expected_output):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_language()
                assert output is not None, "Expected get_language() to return output. Instead, it returned None"
        
        @pytest.mark.parametrize("input_value,expected_output", [
        (2, "JavaScript")])
        def test_is_string(self, input_value, expected_output):
            with patch('builtins.input', return_value=input_value):
                output = gptcoder.get_language()
                assert isinstance(
                output, str
            ), f"Expected get_language() to return a string. Instead, it returned {output}"

        @pytest.mark.parametrize("input_value,expected_output", [
        (2, "JavaScript")])
        def test_is_language(self, input_value, expected_output):
            with patch('builtins.input', return_value=input_value):
                language_dict = ["Python", "JavaScript", "Java", "C", 
                   "C++", "C#", "TypeScript", "PHP", "Swift", "Ruby"]
                output = gptcoder.get_language()
                assert output in language_dict, f"Expected get_language() to return a programming language. Instead, it returned {output}"
        
        
        


