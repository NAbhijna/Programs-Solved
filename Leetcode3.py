i = 0
j = len(s)-1
while (j>=i):
    s[i], s[j] = s[j], s[i]
    i +=1 
    j -= 1
    break