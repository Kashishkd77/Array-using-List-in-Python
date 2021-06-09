# Add elements of two matrices

# For adding both matrices , their dimensions should be same
list1=[[12,13,4],[8,90,87],[67,6,59]]
list2=[[112,1,4],[0,6,3],[275,1,7]]
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
print()
if flag2 == 1:
    print("Matrix B : Valid")

# Matrix B
print("Matrix B :")
for i in list2:
    print(i)
print()

# Addition Validity (Dimensions of both Matrix A and Matrix B should be same)
if flag1==1 and flag2==1:
    if len_r1==len_r2 and len_c1[0]==len_c2[0]:
        print("Addition of Matrix A and Matrix B : Valid (dimensions same of both matrices)")
    else:
        print("Addition of Matrix A and Matrix B : InValid (dimensions different of both matrices)")
        exit()
print()

# Addition of both the Matrix A + Matrix B :
for i in range(len_r1):
    x = []
    for j in range(len(len_c1)):
        y=list1[i][j]+list2[i][j]
        x.extend([y])
    list3.append(x)
print("Addition of both the Matrix A + Matrix B :")
for i in list3:
    print(i)