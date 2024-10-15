import random
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)
def Title():
    print(Fore.GREEN + """
      
$$$$$$$$\                                         $$\   $$\           $$\       $$\                         
\__$$  __|                                        $$ |  $$ |          $$ |      $$ |                        
   $$ | $$$$$$\ $$\   $$\$$$$$$\   $$$$$$$\       $$ |  $$ | $$$$$$\  $$ | $$$$$$$ | $$$$$$\  $$$$$$\$$$$\  
   $$ |$$  __$$\\$$\ $$  \____$$\ $$  _____|      $$$$$$$$ |$$  __$$\ $$ |$$  __$$ |$$  __$$\ $$  _$$  _$$\ 
   $$ |$$$$$$$$ |\$$$$  /$$$$$$$ |\$$$$$$\        $$  __$$ |$$ /  $$ |$$ |$$ /  $$ |$$$$$$$$ |$$ / $$ / $$ |
   $$ |$$   ____|$$  $$<$$  __$$ | \____$$\       $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$   ____|$$ | $$ | $$ |
   $$ |\$$$$$$$\$$  /\$$\$$$$$$$ |$$$$$$$  |      $$ |  $$ |\$$$$$$  |$$ |\$$$$$$$ |\$$$$$$$\ $$ | $$ | $$ |
   \__| \_______\__/  \__\_______|\_______/       \__|  \__| \______/ \__| \_______| \_______|\__| \__| \__|      
    
      
      

        """)
Title()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def play():
    clear()
    number_of_bots = int(input("¿Contra cuántos bots jugarás? (Max 20) >> "))
    suits = ["♥️","♦️", "♠️", "♣️"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards = [f"{rank}{suit}" for suit in suits for rank in ranks]
    random.shuffle(cards)
    
    player1_hand = cards[:2]
    hands = [player1_hand]
    
    house = cards[2:5]
    community_cards = house

    def nextround():
        print(Fore.GREEN + Style.BRIGHT + "Community Cards:", community_cards)
        print(Fore.GREEN + Style.BRIGHT + "Player Hand:", player1_hand)
        print(Fore.YELLOW+ Style.BRIGHT+ """
        1) Check
        2) Fold
        """)
    


    for i in range(number_of_bots):
        bot_hand = cards[5 + i*2 : 7 + i*2]
        hands.append(bot_hand)

    clear()
    Title()
    nextround()
    
    respuesta = input(">>")
    if respuesta == "1":
        print("Opcion n1")
    elif respuesta == "2":
        print("Opcion n2")
    else:
        play()


    clear()
    
    Title()
    new_card = cards[5 + number_of_bots*2]
    community_cards.append(new_card)
    nextround()

    respuesta = input(">>")
    if respuesta == "1":
        print("Opcion n1")
    elif respuesta == "2":
        print("Opcion n2")
    else:
        play()


    clear()
    Title()


    new_card = cards[7 + number_of_bots*2]
    community_cards.append(new_card)
    nextround()


    respuesta = input(">>")
    if respuesta == "1":
        print("Opcion n1")
    elif respuesta == "2":
        print("Opcion n2")
    else:
        play()
    
    for i in range(number_of_bots):
        print(f"Mano del Bot{i+1}:", hands[i+1])

    input("Fin de la partida")
    play()

print("""
 1) Play
 2) Credits
 3) Exit
""")

respuesta = input(">>")
if respuesta == "1":
    play()
elif respuesta == "2":
    print("Created by: U.U")
    input("Presiona Enter para continuar...")
