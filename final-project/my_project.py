from questions import quiz

score = 0

def check_ans(question, ans, attemps, score):
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct answer! \n Your score is {score + 1}!")
        return True
    else:
        print(f"Wrong answer :( \n You have {attemps - 1} attemps left. Try again")
        return False

for question in quiz:
    attemps = 1
    #check = check_ans(question, ans, attemps, score)
    while attemps > 0:
        print(quiz[question]['question'])
        answer = input(f"Please enter answer: ")
        check = check_ans(question, answer, attemps, score)
        if check:
            score += 1
            break
        else:
            score = score
        attemps -= 1
    print(f"Your final score is {score}")

# def check_ans(question, ans, attemps, score):
#     if quiz[question]['answer'].lower() == ans.lower():
#         print(f"Correct answer! \n Your score is {score + 1}!")
#         return True
#     else:
#         print(f"Wrong answer: ( \n Ypu have {attemps - 1} left. Try again")
#         return False
        
#check_ans(question, ans, attemps, score)