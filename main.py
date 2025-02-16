def main():
    print("--- Begin report of books/frankenstein.txt ---")
    #wcount = countWords("frankenstein.txt")
    #wcount_msg = str(wcount) + " words found in the document"
    #print(wcount_msg)
    #alphabet_en = "abcdefghijklmnopqrstuvwxyz"
    dict_fran = countChars("frankenstein.txt")
    char_list_fran = char_count_sort(dict_fran)

    print(str(countWords("frankenstein.txt")) + " words found in the document\n")

    for i in char_list_fran:
        print("The '"+str(i["letter"])+"' character was found "+str(i["num"])+" times")
    
    #print(countChars("frankenstein.txt"))
    print("--- End report ---")

    char_count_sort(dict_fran)

def countWords(booktoopen):
    word_list = []
    word_count = 0
    with open("books/"+booktoopen) as b:
        file_contents = b.read()
        word_list = file_contents.split()
        word_count = len(word_list)
    return word_count
    
def countChars(booktoopen):
    character_count = {}
    with open("books/"+booktoopen) as b:
        file_contents = b.read()
        lowered_strings = file_contents.lower()
        for i in lowered_strings:
            character_count.update({i: 0})
        for y in character_count:
            character_count.update({y: lowered_strings.count(y)})
    #print(character_count)
    return character_count

def sort_on(dictionary):
    return dictionary["num"]

def char_count_sort(dictionary):
    temp_list = []
    for i in dictionary:
        if i.isalpha():
            temp_list.append({"letter": i, "num": dictionary[i]})
    
    temp_list.sort(reverse=True, key=sort_on)
    #for i in range(len(temp_list)):
    #    print(temp_list[i])
    return temp_list

main()