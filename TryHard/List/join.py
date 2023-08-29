thisList1 = ['a', 'b', 'c']
thisList2 = ['1', '2', '3']

#có thể kết hợp hai list lại thành 1 list lớn có 3 cách:

# 1. Dùng '+' 
myList = thisList1 + thisList2
print(myList)

# 2. Dùng append
myList1 = thisList1.copy()
for x in thisList2:
    myList1.append(x)

print(myList1)

# 3. Dùng extend()
myList2 = thisList1.copy()
myList2.extend(thisList2)
print(myList2)
