#MAYOR Y MENOR ENTRE 2 NUMEROS
#Entries
number1= float(input("Enter the first number: "))
number2= float(input("Enter the second number: "))
#Process and outputs
if number1 > number2:
  print(number1, " is the higher number, and ", number2, "is the lower number")
elif number1 < number2:
  print(number2, " is the higher number, and ", number1, "is the lower number")
else:
  print("Both numbers are the same")