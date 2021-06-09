# Perform sum of elements in array

list1=[[23,51,1,8],[111,90,11,7888],[11,67,888,9],[78,90,77,89]]

len_r=len(list1)
len_c=[]           # To store number of columns of each row of given Matrix

# Checking number of columns in each row of given Matrix
for i in range(len_r):
    x=len(list1[i])
    len_c.extend([x])
flag=0

# Matrix Validity (no. of columns of each row should be same)
for i in range(len(len_c)):
    for j in range(i+1,len(len_c)):
        if len_c[i] == len_c[j]:
            flag = 1
        else:
            print("Given Matrix : InValid")
            exit()
print()
if flag==1:
    print("Given Matrix : Valid")
print()

# Given Matrix
print("Given Matrix is : ")
for i in range(len_r):
    for j in range(len_r):
        print(list1[i][j],end=" ")
    print()
print()

# Performing sum of elements in given matrix
sum=0
for i in range(len_r):
    for j in range(len_c[0]):
            sum=sum+list1[i][j]
print("Sum of elements of given matrix is : ",sum)