# Perform intersection operation in 2 array
list1 = [1,23,7,89,231,45,78,11]
list2 = [2,78,23,111,56,78,0,9]
list3=[]
print("List 1 : ",list1)
print("List 2 : ",list2)

length=len(list1)+len(list2)
for i in list1:
   for j in list2:
       if i==j:
            list3.extend([i])
print("Intersection of list 1 and list 2 : ",list3)