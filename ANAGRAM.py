s1 = input("Enter the first string")
s2 = input("Enter the second string")

str1 = s1.lower()
str2 = s2.lower()

a1 = "".join(i for i in str1 if i!=" ")
b1 = "".join(i for i in str2 if i!=" ")

if sorted(a1) == sorted(b1):
    print("The strings are anagrams of each other")
else:
    print("Not anagrams")

