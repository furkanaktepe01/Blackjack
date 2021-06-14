# BLACKJACK
# Single Player
# Moves: Hitting and Standing
# Aces always have the value of 11

from random import shuffle

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shf(self):
        shuffle(self.all_cards)

    def pick_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.cards = []

    def add_cards(self, new_card):
        self.cards.append(new_card)

    def decision(self):
        dec = input(f"Move of {self.name}: ")
        while dec.lower() not in {"hit", "stand", "double down", "split"}:
            print("Invalid move, you can either hit, or stand, or double down, or split")
            dec = input(f"Move of {self.name}: ")
        return dec

    def reset_cards(self):
        self.cards = []


# Game Starts

name_1 = input("Type your name: ")
budget_1 = int(input("Type your budget: "))
player_1 = Player(name_1, budget_1)
the_deck = Deck()
the_deck.shf()
round_num = 0

while True:

    if player_1.budget == 0:
        print(f"{player_1.name} has no money to bet!")
        print("Game is Over!")
        break

    if len(the_deck.all_cards) < 20:
        the_deck = Deck()
        the_deck.shf()

    round_num += 1
    print(f"Round {round_num}")
    round_on = True
    dealers_cards = []
    player_1.reset_cards()

    bet_1 = int(input("Bet: "))
    while bet_1 > player_1.budget:
        print("Your bet cannot exceed your budget!")
        bet_1 = int(input("Bet: "))

    player_1.add_cards(the_deck.pick_one())
    dealers_cards.append(the_deck.pick_one())
    player_1.add_cards(the_deck.pick_one())
    dealers_cards.append(the_deck.pick_one())
    print(f"Dealer: A face-down card and {dealers_cards[1]}")
    print(f"Dealer: {dealers_cards[1].value} + value of face-down card")
    print(f"{player_1.name}: " + " and ".join([x.__str__() for x in player_1.cards]))
    print(f"{player_1.name}: {sum([x.value for x in player_1.cards])}")

    while round_on:

        dec_1 = player_1.decision()

        if dec_1 == "hit":

            player_1.add_cards(the_deck.pick_one())
            print(f"{player_1.name}: " + " and ".join([x.__str__() for x in player_1.cards]))
            print(f"{player_1.name}: {sum([x.value for x in player_1.cards])}")
            if sum([x.value for x in player_1.cards]) > 21:
                print("Bust!")
                print("Dealer: " + " and ".join([x.__str__() for x in dealers_cards]))
                print(f"Dealer: {sum([x.value for x in dealers_cards])}")
                print(f"{player_1.name} lost the round {round_num} and {bet_1}$ !")
                player_1.budget -= bet_1
                print(f"Remaining budget of {player_1.name} is {player_1.budget}")
                round_on = False

        elif dec_1 == "stand":

            print("Dealer: " + " and ".join([x.__str__() for x in dealers_cards]))
            print(f"Dealer: {sum([x.value for x in dealers_cards])}")

            if sum([x.value for x in dealers_cards]) > 21:

                print("Bust!")
                print("Dealer lost!")
                if sum([x.value for x in player_1.cards]) != 21:
                    print(f"{player_1.name} won the round {round_num} and {bet_1}$ !")
                    player_1.budget += bet_1
                    print(f"New budget of {player_1.name} is {player_1.budget}")
                else:
                    print("Blackjack!")
                    print(f"{player_1.name} won the round {round_num} and {3 / 2 * bet_1}$ !")
                    player_1.budget += 3 / 2 * bet_1
                    print(f"New budget of {player_1.name} is {player_1.budget}")
                round_on = False

            elif sum([x.value for x in dealers_cards]) <= 21:

                while sum([x.value for x in dealers_cards]) < 17:

                    dealers_cards.append(the_deck.pick_one())
                    print("Dealer: " + " and ".join([x.__str__() for x in dealers_cards]))
                    print(f"Dealer: {sum([x.value for x in dealers_cards])}")

                else:

                    if sum([x.value for x in dealers_cards]) > 21:

                        print("Bust!")
                        print("Dealer lost!")
                        if sum([x.value for x in player_1.cards]) != 21:
                            print(f"{player_1.name} won the round {round_num} and {bet_1}$ !")
                            player_1.budget += bet_1
                            print(f"New budget of {player_1.name} is {player_1.budget}")
                        else:
                            print("Blackjack!")
                            print(f"{player_1.name} won the round {round_num} and {3 / 2 * bet_1}$ !")
                            player_1.budget += 3 / 2 * bet_1
                            print(f"New budget of {player_1.name} is {player_1.budget}")
                        round_on = False

                    elif sum([x.value for x in dealers_cards]) <= 21:

                        if sum([x.value for x in dealers_cards]) > sum([x.value for x in player_1.cards]):

                            if sum([x.value for x in dealers_cards]) == 21:
                                print("Blackjack!")
                            print("Dealer won!")
                            print(f"{player_1.name} lost the round {round_num} and {bet_1}$ !")
                            player_1.budget -= bet_1
                            print(f"Remaining budget of {player_1.name} is {player_1.budget}")
                            round_on = False

                        elif sum([x.value for x in dealers_cards]) == sum([x.value for x in player_1.cards]):

                            print("Push!")
                            print(f"No one wins on round {round_num} !")
                            print(f"The budget of {player_1.name} is {player_1.budget}")
                            round_on = False

                        elif sum([x.value for x in dealers_cards]) < sum([x.value for x in player_1.cards]):

                            print("Dealer lost!")
                            if sum([x.value for x in player_1.cards]) != 21:
                                print(f"{player_1.name} won the round {round_num} and {bet_1}$ !")
                                player_1.budget += bet_1
                                print(f"New budget of {player_1.name} is {player_1.budget}")
                            else:
                                print("Blackjack!")
                                print(f"{player_1.name} won the round {round_num} and {3 / 2 * bet_1}$ !")
                                player_1.budget += 3 / 2 * bet_1
                                print(f"New budget of {player_1.name} is {player_1.budget}")
                            round_on = False
                    break
    continue
