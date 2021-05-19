#times_ten, la function debe de aceptar  un argumento and display the product
#of its argument multiplied times 10
def main():
    entrada=float(input('Enter the number that will be multiplied by times 10: '))
    times10(entrada)
def times10(number):
    result=number*10
    print('Your times 10 number is: ',result)
main()

#Look at the following function header:
#def my_function(a, b, c):
#Now look at the following call to my_function :
#my_function(3, 2, 1)
#When this call executes, what value will be assigned to a ? What value will be assigned to b ? What value will be assigned to c ?

def my_function(a, b, c):
    print('the value of a is: ',a)
    print('the value of b is: ',b)
    print('the value of c is: ',c)

my_function(3, 2, 1)

#What will the following program display?
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

#Look at the following function definition:

def my_function(a, b, c):
    d = (a + c) / b
    print(d)
my_function(2,4,6)
#a. Write a statement that calls this function and
#uses keyword arguments to pass 2 into a , 4 into b , and 6 into c .
#b. What value will be displayed when the function call executes?
