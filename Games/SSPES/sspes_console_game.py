import random
import json

#stats = {'Won': 0, 'Lost' : 0, 'Draw': 0}
#figures = {0:0, 1:0, 2:0, 3:0, 4:0}

#   0   -   Scissors
#   1   -   Paper
#   2   -   Rock
#   3   -   Lizard
#   4   -   Spock


def random_computer_move():
    return int(random.random()*5)

def strategic_computer_move():
    # key + 2 % 5
    try:
        data = get_data()
        m = max(data, key = data.get)
        return ((int(m) + 2) % 5)
    except:
        random_computer_move()


def game(p):
    beats = {0:[1,3], 1:[2,4], 2:[0,3], 3:[1,4], 4:[0,2]}
    set_data(p)
    c = strategic_computer_move()
    if(c == p):
        set_statistic('Draw') 
        print('You did not beat the computer. The computer did not beat you.')
    elif(c in beats[p]):
        set_statistic('Won') 
        print('You did win!')
    else:
        set_statistic('Lost') 
        print('You did lose!')
    play_game()
    


def get_data():
    with open('figures.json') as json_file:
        data = json.load(json_file)
    return data

def set_data(p):
    data = get_data()
    data[str(p)] += 1
    with open('figures.json', 'w') as f:
        json.dump(data, f)

def upload_data():
    data = get_data()
    for key in data.keys():
        data[key] = data[key] + int(input('How many pulls in ' + key+ '? \n'))

    with open('figures.json', 'w') as f:
        json.dump(data, f)

    console_game()



def get_statistic():
    with open('stats.json') as json_file:
        data = json.load(json_file)
    return data

def set_statistic(k):
    data = get_statistic()
    data[k] += 1
    with open('stats.json', 'w') as f:
        json.dump(data, f)

def show_statistic():
    print(get_statistic())
    console_game()



def play_game():
    p = int(input('0 = Scissors    1 = Paper    2 = Rock   3 = Spock    4 = Lizard \n'))
    game(p)
  

def console_game():
    try:
        p = int(input('0 = Play    1 = Stats    2 = Add Data \n'))
        play_game() if p == 0 else (show_statistic() if p == 1 else upload_data())

    except:
        print('The input was not an valid!')
        console_game()



def main():
    console_game()


if __name__ == "__main__":
    main()