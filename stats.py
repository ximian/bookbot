def get_num_words(booktoopen):
    word_list = []
    word_count = 0
    with open(booktoopen) as b:
        file_contents = b.read()
        word_list = file_contents.split()
        word_count = len(word_list)
    return word_count

def sort_on(tuple_to_sort: tuple[str, int]) -> int:
    return tuple_to_sort[1]

def chars_dict_to_sorted_list(dictionary_to_sort: dict[str, int]) -> list[tuple[str, int]]:
    chars_dict_sorted = []
    for i in dictionary_to_sort:
        chars_dict_sorted.append([i[0], i[1]])
    return chars_dict_sorted.sorted(reverse=True, key=sort_on())