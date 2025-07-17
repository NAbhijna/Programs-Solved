legs = int(input("Enter the total number oflegs: "))
heads = int(input("Enter the total number of heads: "))
flag = False

for hen in range(heads):
    cow = heads-hen
    if(cow*4 + hen*2 == legs):
        print(f"cow: {cow} and hen: {hen}")
        flag = True
        break
if(not flag):
    print("No solution")