#SUMAR O MULTIPLICAR
#Entries
numberA= float(input("Enter the first number: "))
numberB= float(input("Enter the second number: "))
#Process and outputs
if numberA < 0 or numberB < 0:
  print("The addition is: ",numberA+numberB)
else:
  print("The multiplication is: ", numberA*numberB)