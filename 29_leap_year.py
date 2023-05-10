#AÑO BISIESTO
#Entries
year = int(input("Enter the year: "))
#process and Outputs
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
 print(str(year), " is a leap year.")
elif year <=0:
  print("Invalid year")
else:
  print(str(year) + " isn´t a leap year.")