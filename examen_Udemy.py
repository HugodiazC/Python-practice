number=float(input('Enter a number'))

if number<0:
    print(number, 'your number is negativo')
        
else :
    print(number, 'your number is positive')

#segundo ejercicio
#Escribe una secuencia de instrucciones que permitan leer un número
#real por pantalla y que muestre si el número está en el rango entre -5 y 5

number=float(input('Enter a number: '))

if number>-5 and number<5:
    print('your number is between -5 y 5')

else:
    print('your number is not between -5 y 5')
