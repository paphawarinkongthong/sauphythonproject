#โปรแกรมตรวจสอบน้ำหนักรถบรรทุกของด่านชั่งน้ำหนักว่ารถบบรทุกนั้นมีน้ำหนักรถผ่านเกณฑ์หรือไม่ หากน้ำหนักเกิน 1000 kg ลงมาให้แสดงข้อความว่า "รถน้ำหนักผ่านเกณฑ์"โดยให้ป้อนทะเบียนรถบรรทุก และน้ำหนักรถบรรทุกทางแป้นพิมพ์

#วิเคราะห์
#มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อจะไปสร้างเป็น function
#รับค่าทะเบียนรถ น้ำหนักรถ ->inputCarDetial
#ตรวจสอบน้ำหนักรถ และเเสดงผล -> checkCarAndShowWeight

def inputCarDetail() :
    carNo = input('ป้อนทะเบียนรถ : ')
    carweight = float(input('ป้อนน้ำหนักรถ: '))
    return carNo, carweight

def checkCarAndShowwehight(carNo,carWeight) :
    if carWeight > 1000 :
        print(f'{carNo} น้ำหนักไม่ผ่านเกณฑ์')
    else :
        print(f'ทะเบียนรถ{carNo}น้ำหนักผ่านเกณฑ์')

print('--------------------------------')
print('*****--* Truck Checker *--*****')
print('--------------------------------')
carNo,carWeight = inputCarDetail()
print('--------------------------------')
checkCarAndShowwehight(carNo,carWeight)
print('--------------------------------')
