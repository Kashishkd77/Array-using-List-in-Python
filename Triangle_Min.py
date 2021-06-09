# Find minimum among TriangleA and TriangleB
# Condition to check if triangle exists in the matrix --> No. of rows = No. of columns of the given matrix

list1=[[23,51,1,8],[111,90,11,7888],[11,67,888,9],[78,90,77,89]]

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


min_a=list1[0][0]
for i in range(len_r):
    for j in range(i,len_c[0]):
        if min_a>list1[i][j]:
            min_a=list1[i][j]
print("Minimum element in Triangle A : ",min_a)
print()
min_b=list1[1][0]
for i in range(len_r):
    for j in range(len_c[0]):
        if i>j:
            if min_b>=list1[i][j]:
                min_b=list1[i][j]
print("Minimum element in Triangle B : ",min_b)