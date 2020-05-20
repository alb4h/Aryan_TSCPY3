list = [-1, -2, -3, 4, 5, 6]

def negative_numbers():
    negative_count = 0
    for i in list:
        if i < 0:
            negative_count += i
        elif i > 0:
            negative_count += 0
        print(negative_count)

negative_numbers()