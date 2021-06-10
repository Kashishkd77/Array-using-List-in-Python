# Perform transpose in matrix
# Elements of rows and columns are interchanged in the matrix

list1=[[10,20,30],[40,50,60]]

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

print("Entered matrix :")
for i in list1:
        print(i)
print()

# Performing Transpose
print("Transpose of entered matrix :")
list2=[]
for i in range(len_c[0]):
    x=[]
    for j in range(len_r):
        x.extend([list1[j][i]])
    list2.append(x)
for i in list2:
    print(i)
