def remove_string_from_string(substring, string):
    if substring in string:
        string = string.replace(substring, "")
    return string

print(remove_string_from_string("es", "yeses"))
