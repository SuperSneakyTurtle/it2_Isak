import random as rd

hands: list[str] = ["scissors", "paper", "rock"]
player_input = input(str("WHRITE IN YOUR HAND!"))
random_hand: None
score: int = 0


def randomize_hand() -> str:
     random_hand = hands[rd.randint(0, len(hands)-1)]
     return random_hand

print(randomize_hand())
 

def handle_rules() -> None:
     if player_input in hands:
         if player_input == randomize_hand:
             print("tie")

         elif hands.index(player_input) == hands.index(randomize_hand()) +1 %3:
             print("you win")
             has_won = True
        
         elif hands.index(player_input) == hands.index(randomize_hand()) -1 %3:
             print("you loose")
     else:
         print("invalid input")