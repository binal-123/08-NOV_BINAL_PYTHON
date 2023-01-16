s=open("new_file.txt","r")
fl=s.read()
fl_into_list=fl.split()
print(fl_into_list)

fl_into_list.append("kiwi")
print(fl_into_list)