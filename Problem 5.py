s = input("Enter a string: ")
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(f"Number of vowels: {count_vowels(s)}")