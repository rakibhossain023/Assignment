lst = list(map(int, input("Enter a list of numbers separated by commas: ").split(',')))
def secondLargest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None
print(f"Second largest number: {secondLargest(lst)}")