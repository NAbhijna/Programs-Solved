def digit(num):
    for i in str(num):
        if(not prime(int(i))):
            return False
    return True

def sumd(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return prime(sum)

def prime(num):
    if num<2:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True


for i in range(100, 1000):
    if prime(i) and digit(i) and sumd(i):
        print(i, end=" ")

