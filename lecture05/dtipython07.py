import math

def inputRadius():
    return float(input("พื้นที่วงกลม : "))


def calAreaCircle(r):
    return math.pi * r**2

def calRoundCirle(r):
    return 2 * math.pi * r

def calCuberCicle(r):
    return 4/3 * math.pi * math.pow(r,3)

def showResult():
    r = inputRadius()
    print(f'พื้นที่เป็นวงกลม {calAreaCircle(r):.4f} เส้นรอบวงกลมเป็น {calRoundCirle(r):.4f} ปริมาตรทรงกลมเป็น {calCuberCicle(r):.4f}')

showResult()