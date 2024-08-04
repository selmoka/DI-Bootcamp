longest_word = ""

while True:
    word = input("Please type a word without A: ")

    if "A" not in word and len(word) > len(longest_word):
        longest_word = word
        print(f"Congratulations! The new longest word without A is {longest_word}")