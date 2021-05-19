#Comida, calcular 15% de Tip y 7% de taxes poner en display todo
purchase=float(input('Enter the total purchase: '))
tip=purchase*.15
tax=purchase*.07
total=tip+tax+purchase
print('Tip: ',tip,'State Tax: ',format(tax,'.2f'),'Total: ', total)

#Programa que convierta Celsiuis a Fahrenheit, Formula: F=((9/5)*C)+32
#Enter Celsius and display Fahrenheit
C=float(input('Enter the celsuis number: '))
F=((9/5)*C)+32
print('Fahrenheit temperature is: ',F)

#Number of Shares=1000, sold_stock=32.87 y 33.92
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





