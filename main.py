def main():
    import sys
    from stats import get_num_words
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
        #path_to_book = 'books/frankenstein.txt'
        print("--- Begin report of "+path_to_book+" ---")
        dict_fran = countChars(path_to_book)
        char_list_fran = char_count_sort(dict_fran)

        print("Found " + str(get_num_words(path_to_book)) + " total words\n")

        for i in char_list_fran:
            #print("The '"+str(i["letter"])+"' character was found "+str(i["num"])+" times")
            print("('"+str(i["letter"])+"', "+str(i["num"])+")")
    
        print("--- End report ---")

        char_count_sort(dict_fran)
    
def countChars(booktoopen):
    character_count = {}
    with open(booktoopen) as b:
        file_contents = b.read()
        lowered_strings = file_contents.lower()
        for i in lowered_strings:
            character_count.update({i: 0})
        for y in character_count:
            character_count.update({y: lowered_strings.count(y)})
    return character_count

def sort_on(dictionary):
    return dictionary["num"]

def char_count_sort(dictionary):
    temp_list = []
    for i in dictionary:
        if i.isalpha():
            temp_list.append({"letter": i, "num": dictionary[i]})
    
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list

main()
