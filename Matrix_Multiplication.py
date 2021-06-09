# Perform matrix multiplication of 2 matrices

# Dimensions of Matrix 1 --> x1 * y1
# Dimensions of Matrix 1 --> x2 * y2
# Possible Multiplication --> only when y1 = x2 i.e. , Number of column of first matrix should be equal to Number of rows of second matrix
# Resulting Matrix --> Matrix with dimensions x1 * y2

list1=[[2,10],[4,12],[8,81]]
list2=[[1,2,3,4],[3,4,5,6]]
list3=[]

len_r1=len(list1)
len_r2=len(list2)
len_c1=[]           # To store number of columns of each row of Matrix A
len_c2=[]           # To store number of columns of each row of Matrix B

# Checking number of columns in each row of Matrix A
for i in range(len_r1):
    x=len(list1[i])
    len_c1.extend([x])
#print(len_c1)

# Checking number of columns in each row of Matrix B
for i in range(len_r2):
    x=len(list2[i])
    len_c2.extend([x])
#print(len_c2)

flag1=0
flag2=0

# Matrix A Validity (no. of columns of each row should be same)
for i in range(len(len_c1)):
    for j in range(i+1,len(len_c1)):
        if len_c1[i] == len_c1[j]:
            flag1 = 1
        else:
            print("Matrix A : InValid")
            exit()
if flag1==1:
    print("Matrix A : Valid")

# Matrix A
print("Matrix A :")
for i in list1:
    print(i)
print()

# Matrix B Validity (no. of columns of each row should be same)
for i in range(len(len_c1)):
    for j in range(i + 1, len(len_c1)):
        if len_c1[i] == len_c1[j]:
            flag2 = 1
        else:
            print("Matrix B : InValid")
            exit()
if flag2 == 1:
    print("Matrix B : Valid")

# Matrix B
print("Matrix B :")
for i in list2:
    print(i)
print()

# Multiplication Validity (no. of columns of Matrix A and no. of rows of Matrix B should be same)
if flag1==1 and flag2==1:
    if len_r2==len_c1[0]:
        print("Multiplication of Matrix A and Matrix B : Valid (correct dimensions of matrices for their multiplicaton)")
    else:
        print("Multiplication of Matrix A and Matrix B : InValid (problem in dimensions of matrices for their multiplicaton)")
        exit()
print()

# Matrix Multiplication
for i in range(len_r1):
    x = []
    for j in range(len_c2[0]):
        sum=0
        for k in range(len_r2):                     # can also take "len_c1[0]" in place of "len_r2"
            sum = sum + list1[i][k] * list2[k][j]
        x.extend([sum])
    list3.append(x)
print()

print("Matrix A * Matrix B :")
for i in list3:
    print(i)