edit1 = "******"
edit2 = "      "

import random as rn

def wincheck(play1, play2):
    if play1 == "paper" and play2 == "rock":
        return 1
    elif play1 == "rock" and play2 == "scissor":
        return 1
    elif play1 == "scissor" and play2 == "paper":
        return 1
    elif play1 == play2:
        return 2
    else:
        return 0


def PlayerWithBot():
    play1 = 0
    play2 = 0

    for run in range(3):
        player = input(f"\n{edit2} Select [ROCK,PAPER,SCISSOR]: ").lower()
        bot = rn.choice(["ROCK","PAPER","SCISSOR"]).lower()
        print(f"{edit2} Bot choose {bot} ")
        print()
        if wincheck(player,bot) == 1:
            print(f'{edit1} Round {run+1} win player1 {edit1}')
            play1 +=1
        elif wincheck(player,bot) == 2:
            print(f'{edit1} Round {run + 1} is Tie {edit1}')
        else:
            print(f'{edit1} Round {run + 1} win player2 {edit1}')
            play2 += 1

    if play1 > play2:
        print(f"\n{edit1} PLAYER1 WON THE MATCH ;)")
    elif(play1 < play2):
        print(f"\n{edit1} PLAYER2 WON THE MATCH ;)")
    elif play1 == play2:
        print(f"\n{edit1} MATCH IS TIE :) {edit1}")


def Player1WithPlayer2():
    play1 = 0
    play2 = 0

    for run in range(3):
        player1 = input(f"\n{edit2} Select Player1 [ROCK,PAPER,SCISSOR]: ").lower()
        player2 = input(f"\n{edit2} Select Player2 [ROCK,PAPER,SCISSOR]: ").lower()

        print()
        if wincheck(player1, player2) == 1:
            print(f'{edit1} Round {run + 1} win player1 {edit1}')
            play1 += 1
        elif wincheck(player1, player2) == 2:
            print(f'{edit1} Round {run + 1} is Tie {edit1}')
        else:
            print(f'{edit1} Round {run + 1} win player2 {edit1}')
            play2 += 1

    if play1 > play2:
        print(f"\n{edit1} PLAYER1 WON THE MATCH ;)")
    elif (play1 < play2):
        print(f"\n{edit1} PLAYER2 WON THE MATCH ;)")
    elif play1 == play2:
        print(f"\n{edit1} MATCH IS TIE :) {edit1}")

if __name__ == '__main__':

    while 1:
        print()
        print(edit1, " 1: Play with friend ", edit1)
        print(edit1, " 2: Play with computer ", edit1)

        inp = int(input(edit2 + "Enter yoyr Choice: "))

        if inp == 1:
            Player1WithPlayer2()
        else:
            PlayerWithBot()

        # to continue or not
        ch = input(f"\n{edit2}Want to continue [y/n]: ")
        if ch == 'n' or ch == 'N':
            break

