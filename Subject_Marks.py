student = [[0 for i in range(5)] for i in range(5)]
for i in range(5):
    print("-------------------------------------")
    name = input(f"Enter the name of student {i+1}: ")
    student[i][0] = name
    sum = 0
    for j in range(1,4):
        a = int(input(f"Enter the mark for subject {j}: "))
        student[i][j] = a
        sum += a
    percentage = sum //3
    student[i][4] = percentage

print("-------------------------------------")  
for i in range(5):
        print(f"{i+1}. {student[i][0]} : {student[i][4]}%")