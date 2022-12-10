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


def upload_data(data):
    pint(dict(data))
    for l in len(figures):
        figures[l] =+ data[0]
    console_game()


def get_statistic():
    print(stats)
    console_game()


def play_game():
    try:
        try:
            p = int(input('Coose!: 0 = Rock    1 = Paper    2 = Scissors    3 = Spock    4 = Lizard'))
            game(p)
        except:
            print('The input was not an valid!')

    except:
        print('End of the game')
    console_game()


def console_game():
    try:
        p = int(input('Coose!: 0 = Play    1 = Stats    2 = Add Data'))
        print(p)
        play_game() if p == 0 else (get_statistic() if p == 1 else upload_data(input('Copy your stats and paste them here!')))

    except:
        print('The input was not an valid!')
        console_game()


def main():
    console_game()


if __name__ == "__main__":
    main()