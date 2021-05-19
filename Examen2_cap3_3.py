#Property Tax, country collects taxes on assesment value of property,
#60% of the property´s actual value. The property Tax is 64 cent per each $100
#of the assement value. Write a program that ask the actual value of a piece
#of property and displays the assessment value and property tax.
#assesssment value= 60% of the actual value
#property Tax=$.64 per each $100 of the assessment value
def main():
    actual_value=float(input('Enter the actual value of the property: '))
    assessment_value(actual_value)
    property_tax(actual_value)
def assessment_value(a_v):
    ass_v=a_v*.60
    print('the assessment value of the property is: ',ass_v)
def property_tax(a_v):
    p_t=(a_v*.60)*.0064
    print('the property tax of the property is: ',p_t)
main()

    
#body mass Index
#Write a program that alculates and displays a person body mass index (BMI)
#the BMI is often udes to determinate whether a person is overweight or
#underweignt for his or her heigt a person´s BMI si calculated with the following
#formula: BMI = weight x 703/heigth**2  // medidas pounds and inches

def main():
    weight_k=float(input('Enter your body weight in kilos: '))
    height_m=float(input('Enter your height in meters: '))
    BMI(weight_k,height_m)
def BMI(w_k,h_m):
    w_p=w_k*2.20462
    h_i=h_m*39.3701
    BMI=w_p*703/((h_i**2))
    print('your BMI is: ',BMI)
main()

#Class A seats $15, Class B seats $12, Class C seats $9, write a program
#that ask how many tickets for each class of seats were sold, and the amount
# of income generated from seats

def main():
    Class_A=float(input('Enter the how many tickets of Class A were sold: '))
    Class_B=float(input('Enter the how many tickets of Class B were sold: '))
    Class_C=float(input('Enter the how many tickets of Class C were sold: '))
    total_sold(Class_A,Class_B,Class_C)
def total_sold(A,B,C):
    total=(A*15)+(B*12)+(C*9)
    print('The total income for the tickets is: $',total)
main()

# per 115 square feet one galon of paint and eight hours of labor is required
# the company charges $20 per hour. Write a program that asks the user to enter
#the square feet of wall space to be painted and the price of the paint per gallon
# the program shoudl display the folling data_:
#the number of gallons of paint required/ the hours o labor required
#the cost of the paint/the labor charges
#the total cost of the paint job

def main():
    squarefeed=float(input('Enter the number of square feed you want to paint: '))
    paint_cost=float(input('Enter the cost per gallon of your paint: '))
    gallon_required(squarefeed)
    labor_hours(squarefeed)
    PaintCost(squarefeed,paint_cost)
    labor_charge(squarefeed)
    total_cost(squarefeed,paint_cost)
def gallon_required(s_f):
    gallon_r=s_f/115
    print('Number of gallons required: ',gallon_r)
def labor_hours(s_f):
    labor_h=(s_f*8)/115
    print('Hours of labor required: ',labor_h)
def PaintCost(s_f,p_c):
    gallon_r=s_f/115
    total_paint_cost=gallon_r*p_c
    print('The total cost of the required paint is: ',total_paint_cost)
def labor_charge(s_f):
    labor_h=(s_f*8)/115
    labor_c=labor_h*20
    print('Labor charges are: ',labor_c)
def total_cost(s_f,p_c):
    gallon_r=s_f/115
    total_paint_cost=gallon_r*p_c
    labor_h=(s_f*8)/115
    labor_c=labor_h*20
    total=labor_c+total_paint_cost
    print('The total cost of the paint job is: $')
main()

#a rentail company must file a monthly sales tax report listing the total sales
#for the month, and the amount of state and county sales tax collected.
#State Tax is 4%, county sales Tax is 2 %
#write a program that asks the user to enter the total sales for the month
#calculate a display the following:
#the amount of county sales Tax
#the amount of state sales Tax
#total sales Tax

def main():
    total_sales=float(input('Enter the total sales of the month: '))
    state_tax(total_sales)
    county_tax(total_sales)
    total_tax(total_sales)
def state_tax(t_s):
    s_tax=t_s*.004
    print('The state tax is: ')
def county_tax(t_s):
    c_tax=t_s*.002
    print('the county tax is: ')
def total_tax(total_sales):
    c_tax=t_s*.002
    s_tax=t_s*.004
    total_t=c_tax+s_tax
    print(

    

    
    
