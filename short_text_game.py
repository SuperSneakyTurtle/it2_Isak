import numpy

inventory = ["stange_rock", "hairpin", "button"]
main_story = ("You find yourself in the middel of a stange forest", "The bushes rumbles near you, and a dangerous looking goblin apears.")
question = (" What do you do?","Check your pockets?")
answer = None
sugested_action = ["inventory"]



def run_game():
    print(main_story[0])
    answer = str(input(question[1] + "Type y for yes, and n for no "))
    check_answer()
    next_story_line(0)
 

def next_story_line(current_story_line: int):
    current_story_line += 1
    print(main_story[current_story_line])

def check_answer():
    print(answer)
    if answer == "y":
        execute_sugested_action()
    elif answer == "n":
        next_story_line(0)
    else:
        print("invalid_answer")

def execute_sugested_action():
    if sugested_action[0]:
        open_inventory()

def open_inventory():
    print("You have:")
    for i in inventory:
        print(i)

run_game()