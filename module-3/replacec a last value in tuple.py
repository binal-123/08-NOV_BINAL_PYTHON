list1=[(10,20,30),(50,80,90),(65,45,60)]
print()
for i in range(len(list1)):
    newlist=list(list1)
    newlist[:-1]=100
    list1[i]=tuple(newlist)
    print(list1)