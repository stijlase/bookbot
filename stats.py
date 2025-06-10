def word_count(book):
    book_text = book.split()
    return len(book_text)


def char_freq(book):
    freq_dict = {}
    book_formatted = book.lower()
    for char in book_formatted:
        if char not in freq_dict:
            freq_dict[char] = 1
        else: 
            freq_dict[char]+= 1
    return freq_dict


def sorted_freq(freq_dict):
    result = []
    for letter in freq_dict:
        if letter.isalpha():
            entry = {"char": letter, "num": freq_dict[letter]}
            result.append(entry)
    result.sort(reverse=1, key = lambda x: x["num"])
    return result