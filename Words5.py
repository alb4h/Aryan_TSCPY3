list = ["again", "alive", "agent", "hi", "nice", "cools"]

def five_letter(list):
    letter_count = 0
    for i in list:
        if len(i) == 5:
            letter_count += 1
    print(letter_count)

five_letter(list)
