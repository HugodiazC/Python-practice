#problema de la página 62 calcular interes y cantidad de dinero
#para tener $10,000.00 en 10 años
future_value=float(input('enter the desire future value: '))
rate=float(input('Enter the annual interest rate: '))
years=float(input('Enter the number of year the money will grow: '))
present_value=future_value/(1+rate)**years #formula
print('you will nedd to deposit this amount: ', present_value)

# se puede cortar el statement con la barra \ así sea operación
#matemática tambien.
print('Monday', 'are sales',\
      'monday too')
print('one')
print('two')
print('three')

print('one',end=' ')
print('two', end=' ')
print('trhee')#esto imprime one two three (end=' ')

print('one',end='')
print('two', end='')
print('trhee')#esto imprime onetwothree (end='')

print('one', 'two', 'three')
print('one', 'two', 'three', sep='') #onetwothree
print('one', 'two', 'three', sep='*')#one*two*three

print('one\ntwo\nthree')# \n salen en diferentes líneas
print('one\ttwo\tthree')# \t los separa entre ellos




