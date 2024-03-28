import pytest
from unittest.mock import patch, MagicMock
from src.gptcoder import GPTCoder

# Fixture for creating a GPTCoder instance with a mock API key
@pytest.fixture
def coder():
    return GPTCoder("mock_api_key", 1, 1, 5, 10)

class Tests:

    api_key = "mock_api_key"

    @staticmethod
    def test_sanity_check():
        expected = True
        actual = True
        assert actual == expected

    # Test to ensure the GPTCoder instance is initialized correctly
    def test_init(self, coder):
        assert coder.api_key == "mock_api_key"
        assert coder.language == "Python"  # Default language
        assert coder.conciseness == 1
        assert coder.commenting == 5
        assert coder.readability == 10

    # Test the static method get_language_name for various language codes
    @pytest.mark.parametrize("language_code, expected_language", [
        (1, "Python"),
        (5, "C++"),
        (10, "Ruby"),
        (99, "Python")  # Default case
    ])
    def test_get_language_name(self, language_code, expected_language):
        assert GPTCoder.get_language_name(language_code) == expected_language

    def test_initialization_with_mock_api_key(self):
        coder = GPTCoder(api_key='mock_api_key')
        assert coder.api_key == 'mock_api_key', "API key should be correctly stored"

    # Test the behavior of setting the language
    @pytest.mark.parametrize("language_code, expected_language", [
        (1, "Python"),
        (2, "JavaScript"),
        (10, "Ruby"),
    ])
    def test_set_language(self, coder, language_code, expected_language):
        coder.set_language(language_code)
        assert coder.language == expected_language

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
