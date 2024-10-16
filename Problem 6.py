a, b = map(int, input("Enter two numbers separated by a comma: ").split(','))
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(f"GCD of {a} and {b} is: {find_gcd(a, b)}")