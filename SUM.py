#using while
x = int(input("number: "))
sum = 0
while(x>0):
    digit = x%10
    sum = sum + digit
    x = x//10
print(sum)

# Sum of digits
sum = 0
a = int(input("number: "))
for i in str(a):
    sum = sum + int(i)
print(sum)