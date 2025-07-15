# Add marks

sum = 0
while(True):
    a = int(input("Enter mark: "))
    if a<=100:
        sum = sum + a
    if a == 0:
        break
print(f"Total is {sum}")