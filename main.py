#if[condition]then
#else[condition]then

menu= int(input("Enter the option to show (17-29): "))
while menu < 17 or menu > 29:
  menu= int(input("Invalid option, enter the option to show (17-29): "))
else:  
  if menu == 17:
    print('Ejecutando ejercicio 17 "Código para saber si un número es positivo o negativo."')
    print('')
    exec(open("17_positivo_negativo.py").read())
  elif menu == 18:
    print('Ejecutando Ejercicio 18 "Programa que lea dos números del teclado y diga cuál es el mayor y cual el menor."')
    print('')
    exec(open("18_mayor_menor.py").read())
  elif menu ==19:
    print('Ejecutando Ejercicio 19 "Programa que lea tres números enteros positivos, y que calcule e imprima en pantalla el menor y el mayor de todos ellos."')
    print('')  
    exec(open("19_mayor_menor.py").read())
  elif menu ==20:
    print('Ejecutando Ejercicio 20 "Calcular el sueldo de los empleados de una empresa."')
    print('')
    exec(open("20_sueldo_empleados.py").read())
  elif menu ==21:
    print('Ejecutando Ejercicio 21 "Dados dos números A y B sumarlos si A es menor a B sino restarlos."')
    print('')
    exec(open("21_suma_o_resta.py").read())
  elif menu ==22:
    print('Ejecutando Ejercicio 22 "Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible."')
    print('')
    exec(open("22_cociente.py").read())
  elif menu == 23:
    print('Ejecutando Ejercicio 23 "numDia es una variable numérica que puede tomar 7 valores, ellos son 1, 2, 3, 4, 5, 6 o 7. Mostar el nombre el nombre del día de la semana que corresponde al valor de la variable numDia."')
    print('')
    exec(open("23_numDia.py").read())
  elif menu == 24:
    print('Ejecutando Ejercicio 24 "Dadas las longitudes de los tres lados de un triángulo determinar si es equilátero o no."')
    print('')
    exec(open("24_tipo_triangulo_medidas.py").read())
  elif menu == 25:
    print('Ejecutando Ejercicio 25 "Dados dos números A y B sumarlos si al menos uno de ellos es negativo en caso contrario multiplicarlos."')
    print('')
    exec(open("25_suma o multplicacion.py").read())
  elif menu == 26:
    print('Ejecutando Ejercicio 26 "Pidiendo el día y el mes de nacimiento mostrar el signo."')
    print('')
    exec(open("26_signo_zodiacal.py").read())
  elif menu == 27:
    print('Ejecutando Ejercicio 27 "Pidiendo el ingreso de la base y la altura de un cuadrilátero, indicar si es cuadrado o rectángulo. Para cualquiera de los dos casos mostrar el perímetro y el área de la figura."')
    print('')
    exec(open("27_cuadrado_o_rectangulo.py").read())
  elif menu == 28:
    print('Ejecutando Ejercicio 28 "Un negocio hace descuentos en las ventas de sus productos. Si la compra es inferior a $100 el descuento es del 5%, si es mayor o igual a 100 y menor a 200 el descuento es del 10% sino será del 15%. Dado el precio de la venta mostrar el descuento realizado en pesos y el precio final con descuento."')
    print('')
    exec(open("28_descuentos_negocio.py").read())
  else:
    menu == 29
    print('Ejecutando Ejercicio 29 "Realizar un algoritmo que determine si un año es bisiesto o no lo es."')
    print('')
    exec(open("29_leap_year.py").read())