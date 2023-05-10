#MAYOR Y MENOR ENTRE 3
#Entries
number1= float(input("Enter the first number: "))
number2= float(input("Enter the second number: "))
number3= float(input("Enter the third number: "))
#Process and outputs
if number1 > number2 > number3:
  print(number1, " is the higher number, and ", number3, "is the lower number")
elif number1 > number3 > number2:
  print(number1, " is the higher number, and ", number2, "is the lower number")
elif number2 > number1 > number3:
  print(number2, " is the higher number, and ", number3, "is the lower number")
elif number3 > number1 > number2:
  print(number3, " is the higher number, and ", number2, "is the lower number")
elif number2 > number3 > number1:
  print(number2, " is the higher number, and ", number1, "is the lower number")
else:
  print(number3, " is the higher number, and ", number1, "is the lower number")