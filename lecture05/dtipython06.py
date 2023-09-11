#return ที่ไม่มีไรต่อท้าย หมายถึง เป็นการบ่งบอกการทำงานนั้นๆ ว่าเสร็จแล้ว
def example():
    print(11111)
    print(22222)
    return
    print(33333)
    print(44444)
    return


# default Parameter มีการกำหนดค่าเริ่มต้นให้กับพารามิเตอร์
def dtitest(x, y, z=20, a=10):
    print(f"{x} + {y} + {z} + {a} = {x + y + z +a}")

dtitest(5,100)