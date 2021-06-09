# TriangleBsum --> In case of 3*3 matrix , TriangleBsum contains elements of index (10,20,21)
# Condition to check if triangle exists in the matrix --> No. of rows = No. of columns of the given matrix

list1=[[10,20,30],[40,50,60],[70,80,90]]

len_r=len(list1)
len_c=[]           # To store number of columns of each row of given Matrix

# Checking number of columns in each row of given Matrix
for i in range(len_r):
    x=len(list1[i])
    len_c.extend([x])
#print(len_c)

flag=0

# Matrix Validity (no. of columns of each row should be same)
for i in range(len(len_c)):
    for j in range(i+1,len(len_c)):
        if len_c[i] == len_c[j]:
            flag = 1
        else:
            print("Given Matrix : InValid")
            exit()
if flag==1:
    print("Given Matrix : Valid")
print()

# Given Matrix
print("Given Matrix is : ")
for i in range(len_r):
    for j in range(len_c[0]):
        print(list1[i][j],end=" ")
    print()
print()

# Triangle Validity (both dimensions of the given matrix should be same)
if flag==1:
    if len_r==len_c[0]:
        print("Given matrix  : Valid to perform further operation(both dimensions of the given matrix are same)")
    else:
        print("Given Matrix : InValid to perform further operation (both dimensions of the given matrix aren't same)")
        exit()
print()

# Triangle B Elements
print("Elements of Triangle B in given matrix : ")
for i in range(len_r):
    for j in range(len_c[0]):
        if i > j:
            print(list1[i][j],end=" ")
    print()
print()

# Calculating sum of elements of Triangle B
print("Sum of elements of Triangle B in given matrix : ",end="")
sum=0
for i in range(len_r):
    for j in range(len_c[0]):
        if i>j:
            sum=sum+list1[i][j]
print(sum)