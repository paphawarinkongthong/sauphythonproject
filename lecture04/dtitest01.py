widht = float(input("ความกว้าง : "))
height = float(input("ความสูง : "))
lenght = float(input("ความยาว : "))
sum = ((lenght * height * 2) +( lenght * widht * 2)+(lenght * 2)) / 5
print(f"กล่องสี่เหลี่ยมให้มีความกว้าง{widht} ยาว {lenght} สูง {height} ต้องใช้สีทั้งหมด {round(sum)} แกลอน ")
print("กล่องสี่เหลี่ยมให้มีความกว้าง",widht,"ยาว", lenght, "สูง" ,height, "ต้องใช้สีทั้งหมด", round(sum),"แกลอน" )
print("กล่องสี่เหลี่ยมให้มีความกว้าง{} ยาว {}ต้องใช้สีทั้งหมด แกลอน ".format(widht,height,round(sum)))