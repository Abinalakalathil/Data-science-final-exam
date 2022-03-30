import numpy as np
n = int(input("Enter the limit: "))
a = []
print("Enter the elements: ")
for i in range(n):
    a.append(int(input()))
print("Before sorting - ")
for i in a:
    print(i)
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[j] < a[i]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print("\nAfter sorting - ")
for i in a:
    print(i, end=" ")