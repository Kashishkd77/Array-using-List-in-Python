# Find minimum and maximum element from two 1-D arrays
# Find minimum and maximum element in 2-D array

list1=[3]
list2=[4]
print("First 1-D Array : ",list1)
print("Second 1-D Array : ",list2)
max=0
for i in list1:
    for j in list2:
        if i>j:
            max=i
            min=j
        else:
            max=j
            min=i
print("Maximum element in both the 1-D array : ",max)
print("Minimum element in both the 1-D array : ",min)
print()

list_2d=[[31,89,3],[58,90000,1000]]

len_r=len(list_2d)
len_c=[]           # To store number of columns of each row of given Matrix

# Checking number of columns in each row of given Matrix
for i in range(len_r):
    x=len(list_2d[i])
    len_c.extend([x])
#print(len_c)

flag=0

# Matrix Validity (no. of columns of each row should be same)
for i in range(len(len_c)):
    for j in range(i+1,len(len_c)):
        if len_c[i] == len_c[j]:
            flag = 1
        else:
            print("Given 2-D Matrix : InValid")
            exit()
if flag==1:
    print("Given 2-D Matrix : Valid")

print("Given 2-D Array : ")
for i in list_2d:
    print(i)
print()

max=list_2d[0][0]
min=list_2d[0][0]

for i in range(len_r):
    for j in range(len_c[0]):
        if list_2d[i][j]>=max:
            max=list_2d[i][j]
        if list_2d[i][j]<min:
            min=list_2d[i][j]
print("Maximum element in multi-dimensional array : ",max)
print("Minimum element in multi-dimensional array : ",min)