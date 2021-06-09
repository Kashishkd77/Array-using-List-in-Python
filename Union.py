# UNION --> Perform union of 2 arrays .
list1 = [1,23,7,89,231,45,78,11]
list2 = [2,78,23,111,56,78,0,9]
list3=[]
print("List 1 : ",list1)
print("List 2 : ",list2)
length=len(list1)+len(list2)
for i in list1:
    list3.extend([i])
for i in list3:
    for j in list2:
        if j in list3:
            continue
        else:
            list3.append(j)
print("Union of List 1 and List 2 : ",list3)