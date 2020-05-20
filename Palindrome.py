def is_palindrome(fruit):
    str1 = ''
    for i in fruit:
        str1 = i + str1
    if str1 == fruit:
        return True
    else:
        return False


print(is_palindrome("yes"))
