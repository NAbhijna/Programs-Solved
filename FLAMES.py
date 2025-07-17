n3 = "RAJU"
n4 = "PAVI"
n1 = list(n3)
n2 = list(n4)
for i in n1:
    if i in n2:
        n1.remove(i)
        n2.remove(i)
num = len(n1)+len(n2)
ans = ['F', 'L', 'A', 'M', 'E', 'S']
index = 0
while len(ans)!= 1:
    index = (index + (num-1)) % len(ans)
    ans.pop(index)
print("The relation is ", ans[0])