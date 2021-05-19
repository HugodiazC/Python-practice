#piedra=1 papel=2 tijera=3
import random
def verificador(person_choice,computer_choice): 
    if computer_choice ==1 and person_choice==2:
        return'You win.'
    elif computer_choice ==1 and person_choice==3:
        return'Computer wins.'
    elif computer_choice ==2 and person_choice==3:
        return'You win.'
    elif computer_choice ==2 and person_choice==1:
        return'Computer wins.'
    elif computer_choice ==3 and person_choice==2:
        return'Computer wins.' 
    elif computer_choice ==3 and person_choice==1:
        return'You win.'
    elif computer_choice == person_choice:
        return'Tie!, try again.'
        P_C=(input('enter you option ROCK, PAPER or SCISSORS: '))
        computer_choice=random.randint(1,3)
        person_choic=number_translate(P_C)
        print('Computer choice is: ',computer_print_choice(computer_choice))
        print(verificador(person_choic,computer_choice)

def number_translate(computer_choice):
    if computer_choice=='ROCK':
        return 1
    elif computer_choice=='PAPER':
        return 2
    elif computer_choice=='SCISSORS':
        return 3
def computer_print_choice(computer_c):
    if computer_c==1:
        return 'ROCK'
    elif computer_c==2:
        return 'PAPER'
    elif computer_c==3:
        return 'SCISSORS'   
def main():
    P_C=(input('enter you option ROCK, PAPER or SCISSORS: '))
    computer_choice=random.randint(1,3)
    person_choic=number_translate(P_C)
    print('Computer choice is: ',computer_print_choice(computer_choice))
    print(verificador(person_choic,computer_choice))
main()
