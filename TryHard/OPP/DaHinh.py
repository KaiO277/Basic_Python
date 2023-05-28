class HV():
    def __init__(self, dai, rong) :
        self.dai = dai
        self.rong = rong

    def area(self):
        return self.dai * self.rong    

class HT():
    def __init__(self, r):
        self.br = r     

    def area(self):
        return self.br * 3.14
    
def calculate_area(share):
    return share.area()

hv1 = HV(2,3)
t1 = HT(3)

print(calculate_area(hv1))
print(calculate_area(t1))