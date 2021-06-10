import random

def user_input():

    choices = ["r", "p", "s"]
    my_action = input("Enter you choice! (r, p, s)")
    pc_actions = random.choice(choices)
    print(f'Your choose {my_action}, computer choise is {pc_actions}.')
    print("Hi")

    #if my_action == pc_actions:
        #print("Tie")
    beats = {
        "p" : "s",
        "r" : "p",
        "s" : "r"
    }


    if my_action == beats[pc_actions]:
        print(f'I win').format(my_action, pc_actions)

    elif pc_actions == beats[my_action]:
        print(f'Computer wins').format(pc_actions, my_action)

    else:
        print("Tie")


user_input()