book = "frankenstein"

with open(f"books/{book}.txt") as f:

    print(f"Generating report for \"{book}\"")

    file_contents = f.read()
    words = file_contents.split()

    print(f"Word count: {len(words)}")

    letter_count_dict = {}
    for char in file_contents:
        key = char.lower()
        if key in letter_count_dict:
            letter_count_dict[key] += 1
        else:
            letter_count_dict[key] = 1
    
    tuples_list = []
    for key in letter_count_dict.keys():
        if key.isalpha():
            tuples_list.append((key, letter_count_dict[key]))
    
    def myFunc(tuple):
        return tuple[1]

    tuples_list.sort(key=myFunc, reverse=True)

    print("Letter count: ")
    for tuple in tuples_list:
        print(f"{tuple[0]}: {tuple[1]}")


    

