def get_num_words(booktoopen):
    word_list = []
    word_count = 0
    with open(booktoopen) as b:
        file_contents = b.read()
        word_list = file_contents.split()
        word_count = len(word_list)
    return word_count
