a = []

# Nhập số phần tử mảng
n = int(input("Nhập số lượng phần tử mảng: "))

# Nhập giá trị của từ giá trị trong mảng
for i in range(n):
    value = int(input("Nhập phần tử thứ {}: ".format(i)))
    a.append(value)

# In giá trị có trong mảng
for i in range(len(a)):
    print(a[i]) 