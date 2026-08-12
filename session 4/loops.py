object = range(5)
# input("Type a thing: ")
for letter in object:
    letter_to_print = letter
    if (letter == 'p'):
        letter_to_print = letter_to_print.upper()
    print(letter_to_print)