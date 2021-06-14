import random
import operator


guess_choices = "r", "p", "s"
#pincorect_user_input = True
#pc_guess = random.choice(guess_choices)

#print(pc_guess)

def pc_game():
    pc_guess = random.choice(guess_choices)
    print(f'pc guess {pc_guess}')

    return pc_guess


def game():

    while True:

        my_guess = input("Please enter  your guess (r, p, s): ").lower()
        if my_guess == "":
            break

        if my_guess == "r" or my_guess == "p" or my_guess == "s":
            break
        else:
            print(f'Wrong entry {my_guess}')
        

    #print(f'My choice is {my_guess}')
    return my_guess
        


def logic():
        
    winning = {
        "r" : "s",
        "p" : "r",
        "s" : "p"
    }
    # for k, v in winning.items():
    #     print("{} ({})".format(k, v))
    #allows to see the pairs

    #user_choice = game()
    pc_choice = pc_game()
    user_choice = game()
    #order matters when call functions if you want to see comp choice

    if user_choice == "":
        return [-1, -1]

    elif user_choice == winning[pc_choice]:
        print("{} loosing {}, pc win".format(user_choice, pc_choice))
        move = [0, 1]

    elif pc_choice == winning[user_choice]:
        print("{} loosing {}, you win".format(pc_choice, user_choice))
        move = [1, 0]

    else:
        print("Tie")
        move = [0, 0]

    #print(move)
    return move



#logic()

def main():

    score_count = [0, 0]
    max_score = 0
    game_logic = [0, 0]


    while max_score < 5 and score_count[0] <= 2 and score_count[1] <= 2 and game_logic != [-1, -1]:
        game_logic = logic()

        if game_logic == [-1, -1]:
            break

        if max_score == 0:
            score_count = list(map(operator.add, score_count, game_logic))
        else:
            score_count = list(map(operator.add, score_count, game_logic))

        #print(f'Score count is {score_count}')

        max_score = max_score + 1
        print(f'Games played: {max_score}')

    
    print("Done!")
    print(f'Your score is {score_count[0]} and pc score is {score_count[1]}')



main()
