# Merging two matrices
# Matrices valid
list1=[[10,20,30],[40,50,60],[70,80,90]]
list2=[[11,22,33],[44,55,66],[77,88,99]]
len_r1=len(list1)
len_c1=len(list1[0])
len_r2=len(list2)
len_c2=len(list2[0])
if len_c1==len_c2:
        print("Merging possible in given matrices")
else:
    print("Merging not possible in given matrices")
    exit()
print()
print("Entered Matrix A :")
for i in range(len_r1):
    for j in range(len_c1):
        print(list1[i][j],end=" ")
    print()
print()
print("Entered Matrix B :")
for i in range(len_r2):
    for j in range(len_c2):
        print(list2[i][j],end=" ")
    print()
print()
print("Matrix A after merging Matrix B in it : ")
for i in range(len_r2):
    x=[]
    for j in range(len_c2):
        x.extend([list2[i][j]])
    list1.append(x)
for i in list1:
    print(i)
print()
list1=[[10,20,30],[40,50,60],[70,80,90]]
list2=[[11,22,33],[44,55,66],[77,88,99]]
list3=[]
print("Merging Matrix A and Matrix B in new Matrix C : ")
for i in range(len_r1):
    x=[]
    for j in range(len_c1):
        x.extend([list1[i][j]])
    list3.append(x)
for i in range(len_r2):
    x=[]
    for j in range(len_c2):
        x.extend([list2[i][j]])
    list3.append(x)
for i in list3:
    print(i)
