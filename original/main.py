"""
topTrumps.py By James Robinson
Copyright James Robinson 2018 - 2019
All rights reserved.

Please use with jamlib.py version 1.1 or higer
"""

import jamlib as jl
from random import randint
import random
import jarlogs
import time
from console_progressbar import ProgressBar

DEBUG = False
FORCE_RESULT = [True, "D"]  # [D]raw, [C]omputer, [P]layer
CARD_ID = 0
TURN_ID = 0
SETTINGS = {"numofcards":6, "maxskill":300}

if DEBUG: jl.reset()
jl.print_file("menu")

class Card:
    def __init__(self, name="NA", strength=100000, intelligence=0, wisdom=0, power=0):
        global CARD_ID
        
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.power = power
        self.id = CARD_ID
        CARD_ID += 1

    def random_assign(self):
        while self.strength + self.intelligence + self.wisdom + self.power >= SETTINGS["maxskill"]:
            self.strength, self.intelligence, self.wisdom, self.power = randint(0, 100), randint(0, 100), randint(0,100), randint(0, 100)

        self.name = jl.rand_from_file("names.txt")

    def __str__(self):
        return ("\nNAME: {}\nSTRENGTH: {}\nINTELLIGENCE: {}\nWISDOM: {}\nPOWER: {}\n".format(self.name, self.strength, self.intelligence, self.wisdom, self.power))


class Player:
    def __init__(self, human=False):
        self.deck = []
        for i in range(0, SETTINGS["numofcards"]):
            c = Card()
            c.random_assign()
            self.deck.append(c)
        self.name = ""

        self.human = human
        if human and DEBUG == False:
            self.name = jl.string_input("\nEnter your name: ")

        def show_card():
            print(self.deck[0])

    def donald(self):
        # TopTrump AI
        # [1] Strength        [3] Wisdom
        # [2] Intelligence    [4] Power
        option = 0
        best = 0

        if self.deck[0].strength > best: option = 1
        if self.deck[0].intelligence > best: option = 2
        if self.deck[0].wisdom > best: option = 3
        if self.deck[0].power > best: option = 4

        return str(option)


    def get_option(self):
        if self.human:
            print("Your card is:\n", self.deck[0])
            jl.print_file("cat_ops")
            return input("")

        else:
            return self.donald()


def card_battle(player_card, computer_card, category):
    if category == "1":
        if player_card.strength > computer_card.strength:
            return "P"
        elif player_card.strength == computer_card.strength:
            return "D"
        else:
            return "C"

    if category == "2":
        if player_card.intelligence > computer_card.intelligence:
            return "P"
        elif player_card.intelligence == computer_card.intelligence:
            return "D"
        else:
            return "C"

    if category == "3":
        if player_card.wisdom > computer_card.wisdom:
            return "P"
        elif player_card.wisdom == computer_card.wisdom:
            return "D"
        else:
            return "C"

    if category == "4":
        if player_card.power > computer_card.power:
            return "P"
        elif player_card.power == computer_card.power:
            return "D"
        else:
            return "C"
    else:
        print("WRONG INPUT: ROUND FORFEITED")
        return "C"


playAgain = True
while playAgain:
    # Player initilisation
    player1 = Player(human=True)
    computer = Player()

    playerTurn = True
    result = ""

    while True:
        jarlogs.deck(player1, computer, TURN_ID, result)
        if DEBUG: print(f"==========\nTurn = {TURN_ID}")
        if len(player1.deck) == 0 or len(computer.deck) == 0: break

        print(f"\nYou have {len(player1.deck)} cards\n")

        if playerTurn:
            result = card_battle(player1.deck[0], computer.deck[0], player1.get_option())

        else:
            result = card_battle(player1.deck[0], computer.deck[0], computer.get_option())

        # Delay
        pb = ProgressBar(total=100,prefix='BATTLE!', suffix='', decimals=3, length=40, fill='=', zfill=' ')
        p = 0
        if DEBUG: p = 100
        while p < 100:
            pb.print_progress_bar(p)
            p += 1.3846
            time.sleep(0.04)

        pb.print_progress_bar(100)
        print("\n")

        # Force result for debuging
        if FORCE_RESULT[0]: result = FORCE_RESULT[1]

        if DEBUG: print("DBUG: result = ", result)

        # Assigns the next go and transfers card
        # Player won
        if result == "P":
            playerTurn = True
            print(f"{player1.name} won!")

            # Adds card to back of the deck
            player1.deck.append(computer.deck[0])
            del computer.deck[0]

            # Put card to back of deck
            player1.deck.append(player1.deck[0])
            del player1.deck[0]

        # Computer won
        elif result == "C":
            playerTurn = False
            print("Computer won!")

            # Adds card to back of the deck
            computer.deck.append(player1.deck[0])
            del player1.deck[0]

            # Put card to back of deck
            computer.deck.append(computer.deck[0])
            del computer.deck[0]

        # Draw
        elif result == "D":
            print("Draw", end="", flush=True)

            for i in range(0,3):
                time.sleep(0.5)
                print(".", end="", flush=True)
                time.sleep(0.5)

            time.sleep(0.5)
            print("{} and {} were both sent to the".format(player1.deck[0].name, computer.deck[0].name))
            time.sleep(1)
            jl.print_file("gulag")
            print(jl.rand_from_file("punish.txt"))
            time.sleep(2)
            
            del computer.deck[0]
            del player1.deck[0]

        # Unknown result
        else:
            if DEBUG: print("ERROR: UNKNOWN RESULT IN BTL LOOP")

        TURN_ID += 1
    
    # End of game
    # Draw!
    if len(player1.deck) == len(computer.deck):
        print("Draw")

    # Computer won
    elif len(player1.deck) == 0:
        print(f"The computer won in {TURN_ID + 1} turns. \nThe lump of metal, the AI that was programed in less then 30 seconds...")

    # Player won
    elif len(computer.deck) == 0:
        print(f"You won in {TURN_ID + 1} turns!")

    responce = input("Do you want to play again? [y/n]\n")
    if responce[0] == "y" or responce[0] == "Y": playAgain = True
    else: playAgain = False
