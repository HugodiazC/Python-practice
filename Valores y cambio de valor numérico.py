string_value=input('how many hours did you work')
hour=int(string_value)
#convertir valores que eran "string" a valores numéricos (int o float)
hours=int(input('how many hours did you work'))
#el argumento de arroba se sintetiza en el de abajo

#Programa para calcular el precio de descuento de un producto
original_price=float(input('Enter original price'))
discount=original_price*0.2
sale_price=original_price-discount
print('The sale price is:', sale_price)

#cacular promedio
test1=float(input('Enter the firts test score: '))
test2=float(input('Enter the second test score: '))
test3=float(input('Enter the third test score: '))
avegare=(test1+test2+test3)/3
print('the avegare score is: ', avegare)

#Usar signo % (remainder), en este ejercicio
#convertiremos 11370 segundo en horas, minutos y segundos
Total_seconds=float(input('Enter a number o seconds: '))
hours=Total_seconds//3600 #esto es para obtener no. de horas
minutes=(Total_seconds//60)%60 #obtiene no. de minutos
seconds=Total_seconds%60
print('hours: ', hours, 'minutes: ', minutes, 'seconds: ', seconds)

#problema de la página 62 calcular interes y cantidad de dinero
#para tener $10,000.00 en 10 años
future_value=float(input('enter the desire future value: '))
rate=float(input('Enter the annual interest rate: '))
years=float(input('Enter the number of year the money will grow: '))
present_value=future_value/(1+rate)**years
print('you will nedd to deposit this amount: ', present_value)
