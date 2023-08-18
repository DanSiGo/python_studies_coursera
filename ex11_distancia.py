import math

x1 = int(input("digite: "))
y1 = int(input("digite: "))
x2 = int(input("digite: "))
y2 = int(input("digite: "))

d = math.sqrt((x1 - y1)**2) + ((x2 - y2)**2)

if d >= 10:
	print("longe")
else:
	print("perto")