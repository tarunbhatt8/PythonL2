''' Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List] '''

A=[1,2,3,4,5,6,7,8,9]
B=[8,9,23,34,78,90,101]
C=[]
C.extend(A)
C.extend(B)
C.sort()
print("Content of A:\n")
print(A)
print("Content of B:\n")
print(B)
print("Content of C:\n")
print(C)
