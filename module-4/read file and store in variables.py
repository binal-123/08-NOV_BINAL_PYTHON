f1=open("new_file.txt","r")
variable=""
for i in range(1,100):
    variable=variable+f1.read(i)
    print(variable)
