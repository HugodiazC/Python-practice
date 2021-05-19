#describiendo la función def
def message():
    print('hi')
    print('how are you?')
message()

def main():
    print('I have a message for you.')
    message()#llama a la función que es definida despúes
    print('goodbye')
def message():
    print('I am Arthur,')
    print('i am a king')
main()

#otro Uso del main definiendo vario valores

def main():
    star_message()
    input('press enter to step 1')
    step1()
    input('press enter to step 2')
    step2()
    input('press enter to step final')
def star_message():
    print('this is a program')
    print('that help you')
    print()
def step1():
    print('Step 1 is: ...')
    print('move it away...')
    print()
def step2():
    print('step2 is: ')
    print()
main()

#Valores locales son independientes

def main():
    texas()
    california()
def texas():
    birds=5000
    print('texas has',birds,'birds')
def california():
    birds=8000
    print('california has',birds,'birds')
main()

#llamar valores y pasarlo a funciones
def main():
    value=5
    show_double(value)#primero se define acá
def show_double(number):#despues acá se pasa a number)
    result=number*2
    print(result)
main()

#restablecer valores y usar funciones, *global constant*
CONTRIBUTION_RATE=0.05
def main():
    gross_pay=float(input('Enter the gross pay: '))
    bonus =float(input('Enter the amount of bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)
#Cambiar valor de "show_bonus_contrib" al de "gross"
def show_pay_contrib(gross):
    contrib=gross*CONTRIBUTION_RATE
    print('Contribution for gross pay: $',\
          format(contrib,',.2f'),\
    sep='')
#procesar el valor bonus
def show_bonus_contrib(bonus):
    contrib=bonus*CONTRIBUTION_RATE
    print('Contribution for gross pay: $',\
          format(contrib,',.2f'),\
    sep='')
main()

                

        
