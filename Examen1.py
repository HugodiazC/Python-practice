#ejercicios página 76 primer examen 
name=input('what is your name: ')
address=input('what is your address: ')
city=input('city: ')
state=input('state: ')
CP=input('CP: ')
print('your name is: ', name)
print('your address is: ',address,city,state,CP, sep=', ')

Total_sales=float(input ('Enter the total amount of sales: '))
annual_profit=Total_sales*0.23
print('the annual profit for that amount is: ', annual_profit)

Feeds=float(input(' Enter the feed number you want to convert to acres: '))
Acres=Feeds/43560
print('the number of acres is: ', Acres)

item_1=float(input('Insert price of the first item: '))
item_2=float(input('Insert price of the second item: '))
item_3=float(input('Insert price of the third item: '))
item_4=float(input('Insert price of the fouth item: '))
item_5=float(input('Insert price of the fifth item: '))
Tax=(item_1+item_2+item_3+item_4+item_5)*.06
subtotal=(item_1+item_2+item_3+item_4+item_5)-Tax
Total=(item_1+item_2+item_3+item_4+item_5)+Tax
print('subtotal: ',subtotal,'Tax: ',format(Tax,'.2f'),'Total: ',Total)

velocidad_carro=60*1.60934
distance_5=velocidad_carro*5
distance_8=velocidad_carro*8
distance_12=velocidad_carro*12
print('la distancia recorrida en 5 horas es: ', distance_5,'km/h',\
      'la distancia recorrida en 8 horas es: ', distance_8,'km/h',\
      'la distancia recorrida en 12 horas es: ', distance_12,'km/h',)
       

purchase=float(input('Enter the total purchase: '))
state_tax=purchase*.02
country_tax=purchase*.04
total_taxes=state_tax+country_tax
total=purchase+total_taxes
print('the total price is')
print('State Tax: ', state_tax,'Country Tax: ',\
      country_tax,'Total Taxes: ',total_taxes,\
      'Subtotal', purchase,'Total', total)

miles_driven=float(input('Enter the number of kilometers driven: '))
gasoline=float(input('Enter the total of consume liters: '))
MPG=miles_driven/gasoline
print('El rendimiento de tu gasolina es: ',MPG,'kilometros por litro')

purchase=float(input('Enter the total purchase: '))
tip=purchase*.15
tax=purchase*.07
total=tip+tax+purchase
print('Tip: ',tip,'State Tax: ',format(tax,'.2f'),'Total: ', total)

C=float(input('Enter the celsuis number: '))
F=((9/5)*C)+32
print('Fahrenheit temperature is: ',F)

shares1=1000
p_share_1=32.87
commission1=(shares1*32.87)*.02
total_pay=(shares1*32.87)+commission1

shares_sold=1000
p_share_2=33.92
commission2=(shares_sold*33.92)*.02
total_gain=(shares_sold*33.92)

total_pay=shares1*p_share_1
total_sold=shares_sold*p_share_2
total_final=total_gain-total_pay-commission2
float(total_final)

print('The total pay for the stock were: ',total_pay)
print('the total pay commission for teh prochase were: ',commission1)
print('The total sold amount of money is: ',total_sold)
print('The total amount commission for te sold is: ',commission2)
print('The profit for the operation is: ',total_final)

