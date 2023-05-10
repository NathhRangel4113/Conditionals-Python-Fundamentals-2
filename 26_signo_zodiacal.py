#SIGNO ZODIACAL

#Entries
month= str(input("Enter the number of your month of birth (1-12): "))
day= int(input("Enter the day of your birth: "))
#Process and Outputs
while month == "":
  print("El mes no se puede dejar vacio")
  month= int(input("Enter a valid number of month (1-12): "))
  continue
  day= int(input("Enter the day of your birth2: "))
  date= str(day)+ "-"+ str(month)
else: 
  date= str(day)+ "-"+ str(month)
  while month <= 0  or month >= 13: 
      #se valida si es un mes valido
      month= int(input("Enter a valid number of month (1-12): "))
  else:
    if month == 1:
      if day <= 0  or day > 31:
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <=20:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> CAPRICORN <---") 
      else:
        day >= 21 and day <=31
        print("Your date of birth is ", date, "and your zodiac sign is: ---> AQUARIUS <---")
    elif month == 2:
      if day <= 0  or day > 29: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 19:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> AQUARIUS <---")
      else:
        day >= 20 and day <= 29
        print("Your date of birth is ", date, "and your zodiac sign is: ---> PISCES <---")
    elif month == 3:
      if day <= 0  or day > 31: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 20:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> PISCES <---")
      else:
        day >= 21 and day <= 31
        print("Your date of birth is ", date, "and your zodiac sign is: ---> ARIES <---")
    elif month == 4:
      if day <= 0  or day > 30: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 20:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> ARIES <---")
      else:
        day >= 21 and day <= 30
        print("Your date of birth is ", date, "and your zodiac sign is: ---> TAURUS <---")
    elif month == 5:
      if day <= 0  or day > 31: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 20:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> TAURUS <---")
      else:
        day >= 21 and day <= 31
        print("Your date of birth is ", date, "and your zodiac sign is: ---> GEMINI <---")
    elif month == 6:
      if day <= 0  or day > 30: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 20:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> GEMINI <---")
      else:
        day >= 21 and day <= 30
        print("Your date of birth is ", date, "and your zodiac sign is: ---> CANCER <---")
    elif month == 7:
      if day <= 0  or day > 31: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 22:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> CANCER <---")
      else:
        day >= 23 and day <= 31
        print("Your date of birth is ", date, "and your zodiac sign is: ---> LEO <---")
    elif month == 8:
      if day <= 0  or day > 31: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 23:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> LEO <---")
      else:
        day >= 24 and day <= 31
        print("Your date of birth is ", date, "and your zodiac sign is: ---> VIRGO <---")
    elif month == 9:
      if day <= 0  or day > 30: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 22:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> VIRGO <---")
      else:
        day >= 23 and day <= 31
        print("Your date of birth is ", date, "and your zodiac sign is: ---> LIBRA <---")
    elif month == 10:
      if day <= 0  or day > 31: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 23:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> LIBRA <---")
      else:
        day >= 24 and day <= 31
        print("Your date of birth is ", date, "and your zodiac sign is: ---> SCORPIO <---")
    elif month == 11:
      if day <= 0  or day > 30: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 22:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> SCORPIO <---")
      else:
        day >= 23 and day <= 31
        print("Your date of birth is ", date, "and your zodiac sign is: ---> SAGITTARIUS <---")
    else: 
      month == 12
      if day <= 0  or day > 31: 
        day= int(print("Enter a valid date day number: "))
      elif day >= 1 and day <= 21:
        print("Your date of birth is ", date, "and your zodiac sign is: ---> SAGITTARIUS <---")
      else:
        day >= 22 and day <= 31
        print("Your date of birth is ", date, "and your zodiac sign is: ---> CAPRICORN <---")
      