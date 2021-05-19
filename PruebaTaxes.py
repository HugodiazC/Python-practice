item_1=float(input('Insert price of the first item: '))
item_2=float(input('Insert price of the second item: '))
item_3=float(input('Insert price of the third item: '))
item_4=float(input('Insert price of the fouth item: '))
item_5=float(input('Insert price of the fifth item: '))
Tax=(item_1+item_2+item_3+item_4+item_5)*.06
subtotal=(item_1+item_2+item_3+item_4+item_5)-Tax
Total=(item_1+item_2+item_3+item_4+item_5)+Tax
print('subtotal: ',subtotal,'Tax: ',format(Tax,'.2f'),'Total: ',Total)

#distance=speed x time
#carro va a 60 millas por horas, calcular distancia despues de 5 8 y 12 horas
# 1 milla igual a 1.60934 kilometros
velocidad_carro=60*1.60934
distance_5=velocidad_carro*5
distance_8=velocidad_carro*8
distance_12=velocidad_carro*12
print('la distancia recorrida en 5 horas es: ', distance_5,'km/h',\
      'la distancia recorrida en 8 horas es: ', distance_8,'km/h',\
      'la distancia recorrida en 12 horas es: ', distance_12,'km/h',)

#Impuesto del state 2% impuesto de country 4 %, programa que al poner el purchase
#despliege los impuestos state Tax, country tax, total taxes and the total of sale
purchase=float(input('Enter the total purchase: '))
state_tax=purchase*.02
country_tax=purchase*.04
total_taxes=state_tax+country_tax
total=purchase+total_taxes
print('the total price is')
print('State Tax: ', state_tax,'Country Tax: ',\
      country_tax,'Total Taxes: ',total_taxes,\
      'Subtotal', purchase,'Total', total)

#MPG= miles driven / gallons of gas used. Program that ask the user amount of driven miles
#and the number of gallons used y calcular el rendimiento
miles_driven=float(input('Enter the number of kilometers driven: '))
gasoline=float(input('Enter the total of consume liters: '))
MPG=miles_driven/gasoline
print('El rendimiento de tu gasolina es: ',MPG,'kilometros por litro')
