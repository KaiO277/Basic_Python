thisTuper = ('green', 'red', 'black', 'white')

#có 2 cách

#C1: chuyển đổi sang list rồi sử dụng append() để thêm dữ liệu
y = list(thisTuper)
y.append('pink')
thisTuper = tuple(y)
print(thisTuper)

#C2 thêm trực tiếp
x = ('orange',)
thisTuper += x 
print(thisTuper)