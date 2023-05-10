#Variable numDia
#Entries
numDia= float(input("Enter the number of the day of the week to name: "))
#Process and outputs
if numDia== 1:
  print("The day of the week is Monday")
elif numDia== 2:
  print("The day of the week is Tuesday")
elif numDia== 3:
  print("The day of the week is Wednesday")
elif numDia== 4:
  print("The day of the week is Thursday")
elif numDia== 5:
  print("The day of the week is Friday")
elif numDia== 6:
  print("The day of the week is Saturday")
elif numDia== 7:
  print("The day of the week is Sunday")
else:
  numDia<1 or numDia>7
  print('Invalid option menu')