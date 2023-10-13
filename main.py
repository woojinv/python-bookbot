with open("books/frankenstein.txt", "r") as file:
    file_contents = file.read()
    
    # print all the words
    words = file_contents.split()

    word_count_dictionary = {}
    for word in words:
        lower = word.lower()
        key = "".join([char for char in lower if lower.isalpha()])

        if key in word_count_dictionary:
            word_count_dictionary[key] += 1
        else:
            word_count_dictionary[key] = 1
    
    list_of_tuples = []
    for key in word_count_dictionary:
        list_of_tuples.append((key, word_count_dictionary[key]))
    
    sorted_tuples = sorted(list_of_tuples, key=lambda item: item[1], reverse=True)
    for item in sorted_tuples:
        if item[1] > 5:
            print(f"{item[0]}: {item[1]}")
            