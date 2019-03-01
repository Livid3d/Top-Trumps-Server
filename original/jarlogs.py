"""
jarlogs.py By James Robinson
Copyright James Robinson 2018 - 2019
All rights reserved.

Please use with jamlib.py version 1.1 or higer.

This file is not ment to be a liabary but a file for seperating logging functions and other error finding code.
"""

# MODES:
# 1 - Full deck, timestamp and turns
# 2 - Card IDs and turns
# 3 - Turn, current card ID and result

import datetime

LOG_DIR = "Logs//"

LOG_DECK_OPTIONS = 2

def deck(player1, computer, TURN_ID, result):    
    with open(f"{LOG_DIR}deck.log", "a") as file:
        file.write(f"\n==== NEW GAME ====\n")

        if LOG_DECK_OPTIONS == 1:
                # Creates time mark in file
                file.write("\n" + str(datetime.datetime.now()) + " " + str(TURN_ID) + "=" * 50)

                # Loops through players and computers cards
                file.write("\nPLAYER: ========= ")
                for i in player1.deck: file.write(str(i) + str(i.id))
                        
                file.write("\nCOMPUTER ======== ")
                for i in computer.deck: file.write(str(i) + str(i.id))

        elif LOG_DECK_OPTIONS == 2:
                file.write("\n\nTurn: " + str(TURN_ID))
                file.write("\nPLAYER: ========= ")
                for i in player1.deck: file.write(str(i.id)+", ")

                file.write("\nCOMPUTER ======== ")
                for i in computer.deck: file.write(str(i.id)+", ")

        elif LOG_DECK_OPTIONS == 3:
                file.write(f"{result}\n\nTurn: {str(TURN_ID)}" )
                file.write("\nPLAYER: " + str(player1.deck[0]))
                file.write("\nCOMPUTER: " + str(computer.deck[0]))

