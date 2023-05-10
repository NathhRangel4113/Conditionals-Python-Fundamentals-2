#TIPO DE TRIANGULO SEGUN SUS LADOS
#Entries
first_side= float(input("Enter the measure of the first side: "))
second_side= float(input("Enter the measure of the second side: "))
third_side= float(input("Enter the measure of the third side: "))
#Process and outputs
if first_side == second_side and first_side == third_side:
  print("The triangle is equilateral since the measure of all its sides is ", first_side)
elif first_side == second_side or first_side == third_side:
  print("The triangle is isosceles since the measure of two of its sides is ", first_side)
elif second_side == third_side:
  print("The triangle is isosceles since the measure of two of its sides is ", second_side)
elif first_side == 0 or second_side == 0 or third_side == 0:
  print("A triangle cannot have a side with a measure of 0")
else:
  print("The triangle is scalene since the measure of all its sides is different.")