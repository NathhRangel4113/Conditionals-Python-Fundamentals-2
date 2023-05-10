#DESCUENTOS DEL NEGOCIO
#Entries
sales_value= float(input("Enter the sales value in dollars to apply the discount: "))
#Process and outputs
if sales_value > 0 and sales_value <= 100:
  discount1= float((sales_value/100)*5)
  print("The discount made is $", discount1)
  print("The final price is $", sales_value-discount1)
elif sales_value > 100 and sales_value <= 200:
  discount2= float((sales_value/100)*10)
  print("The discount made is $", discount2)
  print("The final price is $", sales_value-discount2)
elif sales_value > 200:
  discount3= float((sales_value/100)*15)
  print("The discount made is $", discount3)
  print("The final price is $", sales_value-discount3)
else:
  sales_value<=0
  print("The value of sales entered does not apply to any discount.")