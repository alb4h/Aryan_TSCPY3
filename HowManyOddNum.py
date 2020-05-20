
list = [1, 2, 3, 4, 5, 6]

def odd_numbers():
    odd_count = 0
    for i in list:
        if i % 2 == 1:
            odd_count += 1
    print(odd_count)

odd_numbers()

