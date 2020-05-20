list = [1, 2, 3, 4, 5, 6]

def even_numbers():
    even_count = 0
    for i in list:
        if i % 2 == 0:
            even_count += i
        elif i % 2 == 1:
            even_count += 0
        print(even_count)


even_numbers()