def remove_from_string(string, occurence):
    for x in string:
        if x in occurence:
            string = string.replace(x, "")
    return string

print(remove_from_string("banana", "a"))