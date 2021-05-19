def main():
      x = 1
      y = 3.4
      print(x, y)
      change_us(x, y)
      print(x, y)
def change_us(a, b):
      a = 0
      b = 0
      print(a, b)
main()

#Programming Exercise #6 in Chapter 2 was the Sales Tax program.
#For that exercise you were asked to write a program that calculates and
#displays the county and state sales tax on a purchase. If you have already
#written that program, redesign it so the subtasks are in functions.
#If you have not already written that program, write it using functions.
purchase=float(input('Enter the total purchase: '))
state_tax=purchase*.02
country_tax=purchase*.04
total_taxes=state_tax+country_tax
total=purchase+total_taxes
print('the total price is')
print('State Tax: ', state_tax,'Country Tax: ',\
      country_tax,'Total Taxes: ',total_taxes,\
      'Subtotal', purchase,'Total', total)
#nuevo ejercicio
def main():
    purchase=float(input('Enter the total purchase: '))
    TAXES(purchase)
    
def TAXES(p):
    sTax=p*.02
    print('State Tax: ', sTax)
    countryTax=p*0.04
    print('country tax: ',countryTax)
    totalTax=sTax+countryTax
    print('Total Taxes: ',totalTax)
    total=totalTax+p
    print('The total is: ',total)
main()

#Many financial experts advise that property owners should insure their
#homes or build-ings for at least 80 percent of the amount it would cost to
#replace the structure. Write a program that asks the user to enter the
#replacement cost of a building and then displays the minimum amount of
#insurance he or she should buy for the property.

def main():
      replacement=float(input('Enter the replacement amount: '))
      insurance(replacement)
def insurance(r):
      insurance=r*.80
      print('the amount for insurance is: ',insurance)
main()

#Automobile Costs
#Write a program that asks the user to enter the monthly costs for the following
#expenses incurred from operating his or her automobile: loan payment, insurance,
#gas, oil, tires, and maintenance. The program should then display the total
#monthly cost of these expenses, and the total annual cost of these expenses.

def main():
      loan_payment=float(input('Enter the monthly cost of the loan payment: '))
      insurance=float(input('Enter the monthly cost of insurance: '))
      oil=float(input('Enter the monthly cost of oil you use: '))
      tires=float(input('Enter the monthly cost of tires: '))
      maintenance= float(input('Enter the cost monthly of maintenance: '))
      loan_anual(loan_payment)
      insurance_anual(insurance)
      oil_anual(oil)
      tires_anual(tires)
      maintenance_anual(maintenance)
      total_cost(loan_payment,insurance,oil,tires,maintenance)
def loan_anual(l_p):
      anual=l_p*12
      print('The monthly cost of loan is: ',anual)
def insurance_anual(ins):
      anual=ins*12
      print('The monthly cost of insurance is: ',anual)
def oil_anual(o):
      anual=o*12
      print('The monthly cost of oil is: ',anual)
def tires_anual(tir):
      anual=tir*12
      print('The monthly cost of tires is: ',anual)
def maintenance_anual(maint):
      anual=maint*12
      print('The monthly cost of oil is: ',anual)
def total_cost(a,b,c,d,e):
      anual=(a+b+c+d+e)*12
      print('The anual cost of all the expenses is: ',anual)
main()

      

      


