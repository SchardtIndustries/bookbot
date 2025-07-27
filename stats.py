def count(text):
    word_count = len(text.split())
    return word_count

def count_characters(text_string):
    char_counts = {}
    for char in text_string:
        lower_char = char.lower()
        if lower_char.isalpha():
            char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    return char_counts

def sort_character_counts(char_counts_dict):
    sorted_list = []
    for char, count in char_counts_dict.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=lambda x: (x["num"]))
    return sorted_list

