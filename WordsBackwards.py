def backwards_words(fruit):
    sz = len(fruit)
    count = 0
    for i in fruit:
        count += 1
        last = fruit[sz-count]
        print(last, end='')


print(backwards_words('yes'))

