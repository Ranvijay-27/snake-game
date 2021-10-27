import pygame as py
import random
import os

py.mixer.init()
py.mixer.music.load(r"R:\pygame\start.mp3")
py.mixer.music.play()

py.init()

screen_width = 900
screen_height = 600

## colour

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

## creating window

gamewindow = py.display.set_mode((screen_width, screen_height))
bgimg = py.image.load(r"R:\pygame\g.jpg")
bgimg = py.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
py.display.set_caption("RANVIJAY")
py.display.update()
font = py.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, color, snak_list, snake_size):
    for x, y in snak_list:
        py.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


## creating the game loof
def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((233, 233, 229))
        text_screen("Welcome to snake game Made By Ranvijay", black, 75, 250)
        text_screen("Press Space Button to Play", red, 120, 420)
        for event in py.event.get():
            if event.type == py.QUIT:
                exit_game = True
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    py.mixer.music.load(r"R:\pygame\backmusic.mp3")
                    py.mixer.music.play()
                    game_loop()
        py.display.update()

        clock = py.time.Clock()
        clock.tick(60)


def game_loop():
    ## game specific variable

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    fps = 60
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 3
    snak_list = []
    snak_len = 1
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    clock = py.time.Clock()
    # font = py.font.SysFont(None,55)

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gamewindow.fill(white)
            text_screen("Game over ! Press Enter to Continue", red, 200 / 2, 400 / 2)
            for event in py.event.get():
                if event.type == py.QUIT:
                    exit_game = True
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:
                        welcome()
        else:

            for event in py.event.get():
                if event.type == py.QUIT:
                    exit_game = True
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RIGHT:
                        # snake_x = snake_x+2
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == py.K_LEFT:
                        # snake_x = snake_x - 2
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == py.K_UP:
                        # snake_y = snake_y - 2
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == py.K_DOWN:
                        # snake_y = snake_y+2
                        velocity_y = init_velocity
                        velocity_x = 0
                        ###chet code
                    if event.key == py.K_q:
                        score += 50

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) <20 and abs(snake_y - food_y) < 20:
                score += 10
                # print(f" score is : {score*10}")

                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snak_len += 5
                if score > int(hiscore):
                    hiscore = score

            gamewindow.fill(black)
            gamewindow.blit(bgimg, (0, 0))
            text_screen("score : " + str(score) + "  hiscore : " + str(hiscore), red, 5, 5)
            py.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snak_list.append(head)

            if len(snak_list) > snak_len:
                del snak_list[0]
            if head in snak_list[:-1]:
                game_over = True
                py.mixer.music.load(r"R:\pygame\gameovermusic.mp3")
                py.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                py.mixer.music.load(r"R:\pygame\gameovermusic.mp3")
                py.mixer.music.play()
                # print("game over")

            plot_snake(gamewindow, white, snak_list, snake_size)

            # py.draw.rect(gamewindow,white,[snake_x,snake_y,snake_size])
        py.display.update()
        clock.tick(fps)

    py.quit()
    quit()


# game_loop()
welcome()