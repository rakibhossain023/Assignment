s = input("Enter a string: ")
def count_digits(s):
    count = sum(c.isdigit() for c in s)
    return count
print(f"Total digits are: {count_digits(s)}")