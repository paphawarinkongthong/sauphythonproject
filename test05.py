celsius = float(input("อุณหภูมิ c: "))
fahrenheit = 9 / 5 * celsius + 32

c = format(float(celsius), ".2f")
f = format(float(fahrenheit), ".2f")

print(f"อุณหภูมิ {celsius:.2f} C อุณหภูมิที่เปลี่ยนแปลง {fahrenheit:.2f} F ")
print("อุณหภูมิ",c, "C", "อุณหภูมิที่เปลี่ยนแปลง", f, "f")
print("อุณหภูมิ" + " "+ c + " C " + "อุณหภูมิที่เปลี่ยนแปลง" + " "+str(f)+" " + "(F)")
print("อุณหภูมิ {:.2f} C อุณหภูมิที่เปลี่ยนแปลง {:.2f}F".format(celsius,fahrenheit))
