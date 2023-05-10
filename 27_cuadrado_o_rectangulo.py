#RECTANGULO O CUADRADO
base = float(input("Enter the base of the quadrilateral: "))
height = float(input("Enter the height of the quadrilateral: "))
area = float(base) * float(height)
perimeter = (base*2)+(height*2)
if base == height:
  print("the quadrilateral is a square")
  print('')
  print("the area is ", area, "and the perimeter is ", perimeter)
elif base == 0 or height == 0:
  print("A quadrilateral cannot have a side that measures 0")
else:
  base != height
  print("the quadrilateral is a square")
  print('')
  print("the area is ", area, "and the perimeter is ", perimeter)