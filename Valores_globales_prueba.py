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
