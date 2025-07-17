a = [23, 129, 45, 200, 45, 34, 27, 77, 88, 127]
sum = 0
count = 0
for i in a:
    if i<100:
        sum += i
        count += 1
print(sum/count)

####################################################

for i in a:
    if(i>100):
        a.remove(i)
print(sum(a)/len(a))