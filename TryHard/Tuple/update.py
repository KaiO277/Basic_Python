#sử dụng list. Chuyển đổi tupper sang list sao đó sửa phẩn tử trong tupper, rồi chuyển đổi về tuper
#tuper là kiểu danh sach không thể thay đổi phần tử trực tiếp được khác list

thisTuper = ('red', 'green', 'white', 'black', 'blue', 'pink')
y = list(thisTuper)
y[1] = 'orange'
x = tuple(y)
print(x)