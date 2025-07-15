# LCM by finding multiples of the bigger number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find the bigger number
bigger = max(a, b)
smaller = min(a, b)

# Start with the bigger number and keep adding it until we find LCM
lcm = bigger

while lcm % smaller != 0:
    lcm += bigger

print(f"LCM of {a} and {b} is: {lcm}")