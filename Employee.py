names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
memo = [0, 1, 1, 1, 2, 2, 1, 2, 1, 2]
salary = [1000, 2000, 3000, 4500, 2000, 5000, 1500, 2300, 1300, 1100]
data = list(zip(names, memo, salary))
removed = [i for i in data if i[2]>4000]
remaining_emp = [i for i in data if i[2]<4000]
remaining_emp = sorted(remaining_emp, key = lambda x:x[2], reverse= True)
another = []
for i in remaining_emp:
    if(i[1]>=2):
        another.append(i)
    if len(another)>3:
        break
print("Removed Employees: ")
for i in removed:
    print(f"Name: {i[0]}, Memo: {i[1]}, Salary : {i[2]}")
for i in another:
    print(f"Name: {i[0]}, Memo: {i[1]}, Salary : {i[2]}")