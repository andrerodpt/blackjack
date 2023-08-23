import random
from art import logo

def blackjack():
    print(logo)

    def deal_card():
        """Returns a random card from the deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    game_ended = False
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards_list):
        """Take a list of cards and return the score calculated"""
        if len(cards_list) == 2 and sum(cards_list) == 21:
            # It's a Blackjack!
            return 0
        else:
            if sum(cards_list) > 21 and 11 in cards_list:
                cards_list.remove(11)
                cards_list.append(1)
            return sum(cards_list)
        
    def show_final_scores():
            print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"\tComputer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack"
        elif user_score == 0:
            return "Win with a Blackjack"
        elif user_score > 21:
            return "Lose. Bust."
        elif computer_score > 21:
            return "Win. Opponent bust."
        elif user_score > computer_score:
            return "Win"
        else:
            return "Lose"

    while not game_ended:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_ended = True
        else:
            print(f"\tYour cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"\tComputer's first cards: {computer_cards[0]}")
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if get_another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_ended = True

    while computer_score != 0 and computer_score < 17 and user_score < 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    show_final_scores()
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n'; ") == 'y':
    blackjack()
