#boolean expresion

y=int(input('Introduzca un número: '))
if y<5:
    print('El no. escrito es menor a 5')
elif y<10:
    print('el no. que escribiste es menor a 10 y mayor o igual a 5')
else:
    print('el no. que escribiste escapa del rango del 1 al 10')
#if es el primer condicionante , elif, segundo y por último else,
    #es a lo que corresponde a cualquier otra cosa. 

#comparing strings
if 'z'< 'a':
    print('z is less than a')
else:
    print('z is not less than a')

if 'New York'< 'Boston':
    print('z is less than a')
else:
    print('z is not less than a')
