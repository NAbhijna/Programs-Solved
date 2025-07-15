s = input("Enter your Password: ")
up = 0
lw = 0
dg = 0
sp = 0
if(len(s)>7):
    for i in s:
        if(i.isupper()):
            up += 1
        elif(i.islower()):
            lw += 1
        elif(i.isdigit()):
            dg += 1
        else:
            sp += 1
    if(up>0 and lw>0 and dg>0 and sp>0):
        print("GOOD PASSWORD")
    else:
        print("BAD PASSWORD")
else:
    print("PASSWORD IS TOO SHORT!!!")