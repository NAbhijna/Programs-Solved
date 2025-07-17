num = [1, 2, 5, 10, 20, 50, 100, 200, 500]
num.sort(reverse=True)

money = int(input("Enter the amount: "))
for i in num:
    while money>=i:
       print(i, end=" ")
       money = money-i
       if money == 0:
           break