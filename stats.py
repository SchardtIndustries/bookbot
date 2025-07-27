def count(text):
    word_count = len(text.split())
    return word_count

def count_characters(text_string):
    char_counts = {}
    for char in text_string:
        lower_char = char.lower()
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    return char_counts
