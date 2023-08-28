# có hai cách  list.remove('truyền vào giá trị mà đc xoá') hoặc list.pod(truyền vào vị trí xoá trong list)
thisList = ["red", "green", "black", "white", "blue"]
thisList.remove("black") #xoá giá trị black trong list
print(thisList)
thisList.pop(1)#xoá vị trí số 1 có giá trị là green trong list, nếu pop() không truyền giá trị nào mặc định lấy giá trị cuối cùng trong list
print(thisList)