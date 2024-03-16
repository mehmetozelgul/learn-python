import math

def is_palindrome(string):
    return string == string[::-1]

test = is_palindrome("radar")
print(test)


