#SUELDO
#Entries
worker_name= input("Enter the name of the worker: ")
hours= float(input("Enter time worked in hours: "))
extra_hours= float(input("Enter the EXTRA time worked in hours: "))
#Process
hour= float(4)
hours*= hour
extra_hours*= hour*2
salary= hours+extra_hours
#Output 
print(worker_name, "´s salary is ", salary, "dollars")                 