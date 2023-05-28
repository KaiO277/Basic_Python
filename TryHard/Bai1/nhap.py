# Nhập phần tử từ bàn phím
# s = input("Nhập một chuỗi cần in: ")

a = int(input("Nhập phần tử a: "))
b = int(input("Nhập phần tử b: "))
action = input("Nhập phép toán bạn cần tính: ")

if (action == "+") :
    s = a + b
elif (action == "-"):
    if (a > b):
        s = a-b
    elif (a < b):
        s = b-a
    else: s=0        
elif (action == "*"):
    s = a * b
else: s = a / b    
print(s)