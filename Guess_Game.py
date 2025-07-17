name1 = input("Enter name ")
name2 = input("Enter name")
player1 = []
player2 = []
s1 = 0
s2 = 0
nums = []
while(len(nums)!=5):
    d = random.randint(1, 100)
    if d not in nums:
      nums.append(d)

for i in range(3):
    ch = input("Enter choice player1")
    if ch in nums:
        s1 += 1
        print("CORRECT")
        player1.append(ch)
    else:
        print("WRONG")
    while(ch in player1 or ch in player2):
        ch = input("Already done retry: ")
        
    ch = input("Enter choice player2")
    if ch in nums:
        s2 += 1
        print("CORRECT")
        player2.append(ch)
    else:
        print("WRONG")
    while(ch in player1 or ch in player2):
        ch = input("Already done retry: ")
        
if s1>s2:
    print("")