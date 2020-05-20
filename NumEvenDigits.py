def num_even_digits(n):
    count = 0
    if n == 0:
        count = 1
    while n != 0:
        if n > 0:
            if n % 2 == 0:
                n = n // 10
                count += 1
            elif n % 2 == 1:
                   n = n // 10
        elif n < 0:
            if n % 2 == 0:
                count += 1
                n = n // -10
            elif n % 2 == 1:

                    n = n // -10


    return count


print(num_even_digits(333))


