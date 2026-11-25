import re


def count_words(text: str) -> int:
    """Count the total number of words in a string.

    Args:
        text: Input string.

    Returns:
        The total count of words.
    """
    if not text:
        return 0
    words = re.findall(r"[^\W_]+(?:'[^\W_]+)?", text)
    return len(words)


def count_word_frequencies(text: str) -> dict[str, int]:
    """Count occurrences of each unique word in the string, case-insensitively.

    Args:
        text: Input string.

    Returns:
        Dictionary mapping lowercase words to their frequencies.
    """
    if not text:
        return {}
    words = re.findall(r"[^\W_]+(?:'[^\W_]+)?", text.lower())
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
