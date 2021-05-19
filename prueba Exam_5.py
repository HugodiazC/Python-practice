def main():
    valid2()
def valid2():
    val1=float(input('Enter a number in range fo 1 to 100: '))
    while val1<1 and val1>100:
        print('ERROR: you should enter a number in range fo 1 to 100')
        val1=float(input('Enter a number in range fo 1 to 100: '))
main()
