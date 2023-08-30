thisSet = {'red', 'green', 'black', 'kk'}

#sử dụng remove()
thisSet1 = thisSet.copy()
thisSet1.remove('red')
print(thisSet1)

#sử dụng discard()
thisSet2 = thisSet.copy()
thisSet2.discard('red')
print(thisSet2)

#sử dụng pop() nhưng sẽ xoá ngẫu nhiên
thisSet3 = thisSet.copy()
thisSet3.pop()
print(thisSet3)

#sử dụng clear
thisSet4 = thisSet.copy()
thisSet4.clear()
print('thisSet4: ',thisSet4)

#sử dụng del sẽ xoá hoàn toàn bào lỗi
thisSet5 = thisSet.copy()
del thisSet5
print(thisSet5)