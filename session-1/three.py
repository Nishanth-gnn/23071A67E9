def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))

