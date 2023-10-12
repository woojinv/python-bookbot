with open("books/raw.githubusercontent.com_asweigart_codebreaker_master_frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    print(len(words))