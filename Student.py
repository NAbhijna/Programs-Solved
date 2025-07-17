student = [[" ", 0] for i in range(5)]
for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    student[i][0] = name
    sum = 0
    for j in range(3):
        a = int(input(f"Enter the mark for subject {j+1}: "))
        sum += a
    percentage = sum //3
    student[i][1] = percentage
    
for i in range(5):
        print(f"{i+1}. {student[i][0]} : {student[i][1]}%")


