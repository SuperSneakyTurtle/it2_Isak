import random as rd

hands: list[str] = ["scissors", "rock", "paper"]
player_input = None
score: int = 0
total_rounds: int = 3
tie: int = 0

def get_player_input():
    global player_input
    player_input = input(str("WHRITE IN YOUR HAND!"))


def handle_rules() -> None:
     global score
     global tie
     get_player_input()
     random_hand = hands[rd.randint(0, len(hands)-1)]
     print(random_hand)
     if player_input in hands:
         if player_input == random_hand:
             print("tie")
             tie += 1

         elif hands.index(player_input) == (hands.index(random_hand) +1) %3:
             print("you win")
             score += 1
        
         elif hands.index(player_input) == (hands.index(random_hand) -1) %3:
             print("you loose")
     else:
         print("invalid input")

for i in range(0, total_rounds):
    handle_rules()
print(f"Your won {score}/{total_rounds} rounds. {tie} round(s) tied")