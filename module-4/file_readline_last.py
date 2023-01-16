with open("next_file.txt",'r') as f:
    for line in f:
        last_line=line
    print(last_line)


with open("test.txt","r") as f:
    for line in f:
        last_line=line
    print(last_line)