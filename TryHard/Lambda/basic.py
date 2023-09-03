#
x = lambda a: a * 2
print(x(5))

#
y = lambda a,b: a + b
print(y(2,5))


#
def my_func(n):
    return lambda a: a*n

z = my_func(2)
w = my_func(3)

print(z(11))
print(w(10))
