thisTuper = ('green', 'red', 'black', 'white', 'pink', 'orange')
# có 2 cách:

#C1: chuyển sang list
y = list(thisTuper)
y.remove('red')
thisTuper = tuple(y)
print(thisTuper)

#C2: sử dụng del trong tuple nhưng sẽ xoá toàn bộ dữ liệu gây ra báo lỗi
del thisTuper