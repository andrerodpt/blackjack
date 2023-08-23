############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_table = {}
game_ended = False
player_phase_done = False
cpu_phase_done = False

def init_game():
    print("init_game() START")
    global game_table
    global game_ended
    global player_phase_done
    global cpu_phase_done
    game_table = {}
    game_ended = False
    player_phase_done = False
    cpu_phase_done = False
    print("init_game() FINISH")

def pick_cards(nr_of_cards):
    cards_delt = []
    for _ in range(nr_of_cards):
        cards_delt.append(random.choice(cards))
    return cards_delt

def dealhand():
    cards_delt = pick_cards(2)
    return cards_delt

def show_final_scores():
    global game_table
    print(f"\tYour final hand: {game_table['player']}, final score: {sum(game_table['player'])}")
    print(f"\tComputer's final hand: {game_table['cpu']}, final score: {sum(game_table['cpu'])}")

def has_ace(hand):
    return hand.index(11) if 11 in hand else -1

def check_result():
    global game_ended
    player_result = sum(game_table['player'])
    cpu_result = sum(game_table['cpu'])
    if cpu_result == 21:
        game_ended = True
        show_final_scores()
        print("Lose, opponent has Blackjack 😱")
    elif player_result == 21:
        game_ended = True
        show_final_scores()
        print("You win! ")
    elif player_result > 21:
        ace_index = -1
        ace_index = has_ace(game_table['player'])
        if ace_index != -1:
            game_table['player'][ace_index] = 1
        else:
            game_ended = True
            show_final_scores()
            print("You lose! ")
    elif cpu_result > 21:
        ace_index = -1
        ace_index = has_ace(game_table['cpu'])
        if ace_index != -1:
            game_table['cpu'][ace_index] = 1
        else:
            game_ended = True
            show_final_scores()
            print("You win! ")
    elif player_phase_done and cpu_phase_done:
        if player_result > cpu_result:
            game_ended = True
            show_final_scores()
            print("You win! ")
        elif player_result < cpu_result:
            game_ended = True
            show_final_scores()
            print("You lose! ")
        else:
            game_ended = True
            show_final_scores()
            print("You draw! ")

def blackjack():
    global game_ended
    global player_phase_done
    global cpu_phase_done

    print(game_table)
    init_game()
    print(game_table)

    print(logo)

    ## Deal Player Hand
    game_table['player'] = dealhand()

    ## Deal CPU Hand
    game_table['cpu'] = dealhand()

    ## We need to check the result after each card delt
    check_result()

    print(f"\tYour cards: {game_table['player']}, current score: {sum(game_table['player'])}")
    print(f"\tComputer's first card: {game_table['cpu'][0]}")
    
    ## Player Phase
    while not game_ended and not player_phase_done:
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if get_another_card == 'y':
            card_picked = pick_cards(1)
            game_table['player'].append(card_picked[0])
            check_result()
            print(f"\tYour cards: {game_table['player']}, current score: {sum(game_table['player'])}")
        else:
            player_phase_done = True  

    ## CPU Phase
    while not game_ended and not cpu_phase_done:
        if sum(game_table['cpu']) < 17:
            card_picked = pick_cards(1)
            game_table['cpu'].append(card_picked[0])
            check_result()
        else:
            cpu_phase_done = True
    
    check_result()

continue_play = True
while continue_play:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n'; ") == 'y':
        blackjack()
    else:
        continue_play = False