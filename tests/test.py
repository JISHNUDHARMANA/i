import pytest
from wordcount import count_words, count_word_frequencies


def test_count_words_basic() -> None:
    """Test counting words in simple sentences."""
    assert count_words("hello world") == 2
    assert count_words("The quick brown fox jumps over the lazy dog.") == 9


def test_count_words_with_punctuation_and_contractions() -> None:
    """Test counting words with punctuation and contractions."""
    assert count_words("Hello, world! It's a sunny day--really sunny.") == 8
    assert count_words("one... two... three! Done.") == 4


def test_count_words_empty_and_whitespace() -> None:
    """Test empty string and whitespace-only string."""
    assert count_words("") == 0
    assert count_words("   \t\n   ") == 0
    assert count_words("!@#$%^&*()") == 0


def test_count_words_single_word() -> None:
    """Test string with a single word."""
    assert count_words("Word") == 1
    assert count_words("   Python   ") == 1


def test_word_frequencies() -> None:
    """Test frequency counting functionality."""
    text = "Hello hello HELLO world World"
    expected = {"hello": 3, "world": 2}
    assert count_word_frequencies(text) == expected
