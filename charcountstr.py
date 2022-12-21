str=input("enter string")
print(str)
x=(list(str))
print(x)
freq=[x.count(ele)for ele in x]
print(freq)
dict=(zip(x,freq))
print(dict)