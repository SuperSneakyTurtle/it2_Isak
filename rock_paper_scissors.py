import random as rd

hands: list[str] = ["scissors", "paper", "rock"]
player_input = None
score: int = 0

def get_player_input():
    global player_input
    player_input = input(str("WHRITE IN YOUR HAND!"))


def handle_rules() -> None:
     global score
     get_player_input()
     random_hand = hands[rd.randint(0, len(hands)-1)]
     print(random_hand)
     if player_input in hands:
         if player_input == random_hand:
             print("tie")

         elif hands.index(player_input) == (hands.index(random_hand) +1) %3:
             print("you win")
             score += 1
        
         elif hands.index(player_input) == (hands.index(random_hand) -1) %3:
             print("you loose")
     else:
         print("invalid input")

for i in range(0, 10):
    handle_rules()
print(f"Your score is: {score}")