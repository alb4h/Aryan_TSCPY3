def count_letters(string, letter):
    fruit = string
    count = 0
    for char in fruit:
        if char == letter:
            count += 1
    return count

print(count_letters("banana", "a"))