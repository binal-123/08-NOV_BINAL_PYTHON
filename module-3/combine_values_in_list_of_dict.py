L=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
from collections import counter
item_list=copy()
result=counter()
for d in item_list:
    result[d['item']] += d['amount']
    print(result)
