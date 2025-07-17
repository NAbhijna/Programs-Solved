count = 0
c = 0
while(c<20):
    for i in range(100, 1000):
        s = i*0.5
        for j in range(2, s):
            if(i%j == 0):
                count += 1
        if(count == 0):
            print(i)
            c+=1
        
