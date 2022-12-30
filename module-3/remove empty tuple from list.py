list=[(),(10,20,234),(),(49,87),(),(1,5)]
for tuple in list:
    if(len(tuple))==0:
        list.remove(tuple)
        print(list)