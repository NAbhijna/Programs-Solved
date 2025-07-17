teams = []
n = int(input("Enter the number of teams: "))
for i in range(n):
    a = input(f"Enter the team name {i+1}: ")
    teams.append(a)
m = int(input("Enter the number of matches"))
match=[]
for i in range(n-1):
    for j in range(i+1, n):
        for k in range(m):
            match.append(teams[i], teams[j])
            
print("----------------")
index = 1
for i in match:
    print(f"{index}. {match[i][0]} vs {match[i][1]}")
    index += 1