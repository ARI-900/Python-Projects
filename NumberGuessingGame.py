# Number guessing:
import  random
pat1 = '******'
pat2 = '      '

def NumberGuessing():
    while 1:
        con = 4
        LuckyNumber = random.choice(range(1, 21))

        for i in range(4):
            val = int(input(f"{pat2} Enter your choice: "))

            if val == LuckyNumber:
                print(f"{pat2} wow, You got the number: ")
                break
            elif (val < LuckyNumber):
                print(f"{pat2} To Low :D")
            elif (val > LuckyNumber):
                print(f'{pat2} To High')
            con -= 1
            if con == 0:
                print(f'{pat1} Well Try Real Number Was: {LuckyNumber} {pat1}')
            else:
                print(f'{pat1} You have remaining {con} chance {pat1}')


        if(input("Want To Try[YES/NO]: ") == 'NO'):
                return



if __name__ == '__main__':

    while 1:
        print("\n")
        print("****** 1: Start the game ******",)
        print("****** 2: Quit the game ******")

        n = int(input(f"{pat2} Enter your choice: "))

        match n:
            case 1:
                print(f'''
                {pat1} Note {pat1}
                1:You got 4 chance to win the game
                2:Number range is always between [1-20]
                ENJOY ;)
                ''')
                NumberGuessing()
            #     After Return
                print(f"\n{pat2} Hope You Enjoy This Game ;)\n")

            case 2:
                exit(0)
                print()
            case __:
                print(f'{pat2} Invalid Input\n')

