s = input("Enter a string: ")
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome(s))