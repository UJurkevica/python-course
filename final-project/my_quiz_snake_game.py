import pygame
import random

pygame.init()

valid_chars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shift_chars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

dis_width = 800
dis_height = 600

black = (0, 0, 0)
red = (152, 90, 90)
grey = (192, 192, 192)
dark_grey = (96, 96, 96)

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 20)

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Quiz improvisation using Snake game!')


class TextBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.text = ""
        self.font = pygame.font.Font(None, 50)
        self.image = self.font.render("Please enter your name here", False, [0, 0, 0])
        self.rect = self.image.get_rect()

    def add_chr(self, char):
        global shiftDown
        if char in valid_chars and not shiftDown:
            self.text += char
        elif char in valid_chars and shiftDown:
            self.text += shift_chars[valid_chars.index(char)]
        self.update()

    def update(self):
        old_rect_pos = self.rect.center
        self.image = self.font.render(self.text, False, [0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.center = old_rect_pos


textBox = TextBox()
shiftDown = False
textBox.rect.center = [400, 300]

running = True
while running:
    dis.fill([209, 185, 185])
    dis.blit(textBox.image, textBox.rect)
    add_notes = font_style.render("If snake exits the window you end quiz.", True, dark_grey)
    add_notes2 = font_style.render("To access the quiz enter your name and hit enter", True, dark_grey)
    add_notes3 = font_style.render("When game window opens press any arrow key to start quiz", True, dark_grey)
    dis.blit(add_notes, [50, 100])
    dis.blit(add_notes2, [50, 150])
    dis.blit(add_notes3, [50, 200])
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYUP:
            if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                shiftDown = False
        if e.type == pygame.KEYDOWN:
            textBox.add_chr(pygame.key.name(e.key))
            if e.key == pygame.K_SPACE:
                textBox.text += " "
                textBox.update()
            elif e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                shiftDown = True
            elif e.key == pygame.K_BACKSPACE:
                textBox.text = textBox.text[:-1]
                textBox.update()
            elif e.key == pygame.K_RETURN:
                if len(textBox.text) > 0:
                    print(textBox.text)
                    running = False



clock = pygame.time.Clock()

snake_block = 20
snake_speed = 10


quiz_questions = [
    "Session 2 topic: ",
    "Session 4 topic: ",
    "Session 6 topic: "]

question_choices = [
    ["A) Variables", "B) Flow Control"],
    ["A) Lists", "B) Functions"],
    ["A) Dictionaries", "B) Mini Project"]
]


def your_score(score, answer, current_questions_set):
    local_score = score
    if answer == "a" and current_questions_set == 0:
        local_score += 1
    elif answer == "b" and current_questions_set == 1:
        local_score += 1
    elif answer == "b" and current_questions_set == 2:
        local_score += 1

    value = score_font.render("Your Score: " + str(local_score), True, black)
    dis.blit(value, [650, 550])
    return local_score


def update_questions(answer, current_questions_set):
    if answer != "":
        if current_questions_set == 0:
            current_questions_set = 1
        elif current_questions_set == 1:
            current_questions_set = 2
        else:
            current_questions_set = 0

    value1 = score_font.render(quiz_questions[current_questions_set], True, black)
    ans1 = score_font.render(question_choices[current_questions_set][0], True, black)
    ans2 = score_font.render(question_choices[current_questions_set][1], True, black)

    dis.blit(value1, [10, 0])
    dis.blit(ans1, [60, 20])
    dis.blit(ans2, [60, 40])
    return current_questions_set


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 5, dis_height / 3])


def message2(msg2, color):
    mesg2 = font_style.render(msg2, True, color)
    dis.blit(mesg2, [dis_width / 5, dis_height / 2])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    food_image_a = pygame.image.load("images/letter-A.png").convert()
    food_image_b = pygame.image.load("images/letter-B.png").convert()
    foodx = round(random.randrange(1, dis_width - snake_block) / snake_block) * snake_block
    foodx2 = round(random.randrange(1, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(3, dis_height - snake_block) / snake_block) * snake_block
    foody2 = round(random.randrange(3, dis_height - snake_block) / snake_block) * snake_block

    last_answer = ""
    currentScore = 0
    current_question_set_id = 0

    while not game_over:

        while game_close == True:
            dis.fill(grey)
            message(str(textBox.text) + " your scored " + str(currentScore) + " points out of " + str(
                len(quiz_questions)) + " questions", red)
            message2("Press C if you want Play Again or Q to Quit", red)
            last_answer = ""
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(grey)
        dis.blit(food_image_a,(foodx, foody, snake_block, snake_block) )
        dis.blit(food_image_b, (foodx2, foody2, snake_block, snake_block))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        if Length_of_snake == 4:
            game_close = True

        our_snake(snake_block, snake_List)
        currentScore = your_score(currentScore, last_answer, current_question_set_id)
        current_question_set_id = update_questions(last_answer, current_question_set_id)
        last_answer = ""

        pygame.display.update()

        if (x1 == foodx and y1 == foody) or (x1 == foodx2 and y1 == foody2):
            if x1 == foodx:
                last_answer = "a"
            else:
                last_answer = "b"

            foodx = round(random.randrange(1, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(3, dis_height - snake_block) / snake_block) * snake_block
            foodx2 = round(random.randrange(1, dis_width - snake_block) / snake_block) * snake_block
            foody2 = round(random.randrange(3, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop()
