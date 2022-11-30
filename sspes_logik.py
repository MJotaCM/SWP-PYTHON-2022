import random

stats = {'Won': 0, 'Lost' : 0, 'Draw': 0}
figures = {0:0, 1:0, 2:0, 3:0, 4:0}

#   0   -   Scissors
#   1   -   Paper
#   2   -   Rock
#   3   -   Lizard
#   4   -   Spock

def computer_move():
    return int(random.random()*5)

def game(p):
    beats = {0:[1,3], 1:[2,4], 2:[0,3], 3:[1,4], 4:[0,2]}
    figures[p] += 1
    c = computer_move()
    if(c == p):
        stats['Draw'] += 1
        print('You did not beat the computer. The computer did not beat you.')
    elif(c in beats[p]):
        stats['Won'] += 1
        print('You did win!')
    else:
        stats['Lost'] += 1
        print('You did lose!')
    print(stats)
    print(figures)

def console_game():
    try:
        p = int(input('Coose!: 0 = Rock    1 = Paper    2 = Scissors    3 = Spock    4 = Lizard'))
        game(p)
    except:
        print('The input was not an valid!')

    if (input('Play Again?') == 'j'):
            console_game()

def main():
    console_game()

if __name__ == "__main__":
    main()