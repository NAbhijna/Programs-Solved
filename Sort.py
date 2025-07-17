a = [10, 12, 11, "Zakir", "Bala", 23, 44, 53, "Anuj", 67, 20, 46, 7, "Jack"]

odd = []
even = []
string = []

for i in a:
    if(type(i)==str):
        string.append(i)
    elif(i%2==0):
        even.append(i)
    else:
        odd.append(i)
    odd.sort()
    even.sort()
    string.sort()
print(odd+even+string)