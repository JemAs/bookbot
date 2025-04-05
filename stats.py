def get_num_words(book):
    words = book.split()
    return words

def get_num_chars(book):
    # Inside the function, you'll need to create a dictionary to store character counts
    lower_chars = book.lower()
    character_counts = {}
    for char in lower_chars:
        if char in character_counts:
            # We've seen this character before, increment its count
            character_counts[char] += 1
        else:
            # First time seeing this character, set count to 1
            character_counts[char] = 1
    return character_counts

def sort_on(dict_of_chars):
    return dict_of_chars["count"]

def get_sorted(dict_of_chars):
    list_of_chars = []
    for char, count in dict_of_chars.items():
        list_of_chars.append({"char": char, "count": count})
    list_of_chars.sort(reverse=True, key=sort_on)
    # Sort the list of dictionaries by count in descending order
    return list_of_chars