import random as rd

hands: list[str] = ["scissors", "paper", "rock"]
player_input = input(str("WHRITE IN YOUR HAND!"))
random_hand: None
score: int = 0

# def execute_functions() -> None:
#     #handle_rules()

# def randomize_hand() -> String:
#     random_hand = hands[rd.randint(0, len(hands)-1)]
#     return random_hand

# #print(randomize_hand())

# def handle_rules() -> None:
#     if player_input in hands:
#         if player_input == randomize_hand:
#             print("tie")
#             add_to_score()

#         elif hands.index(player_input) == hands.index(random_hand()) +1 %3:
#             print("you win")
#             add_to_score()
        
#         elif hands.index(player_input) == hands.index(random_hand()) -1 %3:
#             print("you loose")
#             add_to_score()
#     else:
#         print("invalid input")

# def add_to_score():
#     score += 1
# execute_functions()