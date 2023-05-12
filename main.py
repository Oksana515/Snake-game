import pygame as pg
from random import randint, randrange, choice

pg.init()

clock = pg.time.Clock()

W = 420
H = 420
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Snake')

my_font = pg.font.SysFont(None, 30)


def draw_text(text, font, t_color, x_text, y_text):
    font_img = font.render(text, True, t_color)
    screen.blit(font_img, (x_text, y_text))


BG = 0, 0, 10
line_color = 0, 60, 110
blue = 0, 40, 170
green = 0, 153, 0
red = 153, 0, 76
violet = 76, 0, 153
white = 255, 255, 255
black = 0, 0, 0

colors = [(255, 62, 0), (255, 97, 0), (255, 123, 0), (255, 149, 0), (255, 179, 0), (255, 214, 0), (255, 239, 0)]


def y_down(some_y):
    some_y += snake_speed
    return some_y


def y_up(some_y):
    some_y -= snake_speed
    return some_y


def x_right(some_x):
    some_x += snake_speed
    return some_x


def x_left(some_x):
    some_x -= snake_speed
    return some_x


def change_coord(some_list, some_length):
    for j in reversed(range(some_length - 1)):
        for i in range(2):
            some_list[j + 1][i] = some_list[j][i]


def can_add_block_x_l(s_list, length):
    you_can_add_block = False
    if s_list[length - 2][1] == s_list[length - 1][1] and s_list[length - 2][0] - s_list[length - 1][0] == 20:
        you_can_add_block = True
    return you_can_add_block


def can_add_block_x_r(s_list, length):
    you_can_add_block = False
    if s_list[length - 2][1] == s_list[length - 1][1] and s_list[length - 1][0] - s_list[length - 2][0] == 20:
        you_can_add_block = True
    return you_can_add_block


def can_add_block_y_u(s_list, length):
    you_can_add_block = False
    if s_list[length - 2][0] == s_list[length - 1][0] and s_list[length - 2][1] - s_list[length - 1][1] == 20:
        you_can_add_block = True
    return you_can_add_block


def can_add_block_y_d(s_list, length):
    you_can_add_block = False
    if s_list[length - 2][0] == s_list[length - 1][0] and s_list[length - 1][1] - s_list[length - 2][1] == 20:
        you_can_add_block = True
    return you_can_add_block


x = None
y = None
moving_down = None
moving_up = None
moving_right = None
moving_left = None
snake_speed = None
snake_length = None
food_x = None
food_y = None
snake_list = None
color_list = None
food_eaten = None
game_over = None
snake_color = None


def set_initial_parameters():
    global x, y, moving_down, moving_up, moving_left, moving_right, \
        snake_list, snake_speed, snake_length, food_x, food_y, color_list, food_eaten, game_over, snake_color
    x0 = 200
    y0 = 160
    x = x0
    y = y0
    moving_down = False
    moving_up = False
    moving_right = False
    moving_left = False
    snake_speed = 20
    food_x = 400
    food_y = 240

    snake_list = []
    snake_length = 4
    for i in range(snake_length):
        snake_list.append([x0 - i * 20, y0])
    color_list = []

    food_eaten = False
    game_over = False

    snake_color = randint(0, 250), randint(0, 250), randint(0, 250)


set_initial_parameters()

run = True

while run:

    clock.tick(10)

    screen.fill(BG)

    # for i in range(0, W, 20):
    #     pg.draw.line(screen, line_color, (i, 0), (i, H))
    #     pg.draw.line(screen, line_color, (0, i), (W, i))

    # drawing food
    if not game_over:
        pg.draw.rect(screen, white, (food_x, food_y, 20, 20))

    if game_over:
        draw_text('Game Over', my_font, white, 160, 130)
        draw_text('Your score =', my_font, white, 140, 180)
        screen.blit(my_font.render(str(snake_length - 4), True, white), (270, 180))
        draw_text('Press R to restart', my_font, white, 130, 250)

    # eating food and removing next food to another place
    if snake_list[0][0] == food_x and snake_list[0][1] == food_y:
        food_eaten = True
        food_x = randrange(0, W - 20, 20)
        food_y = randrange(0, H - 20, 20)

    # collision with itself
    for i in range(snake_length - 3):
        if snake_list[0][0] == snake_list[i+3][0] and snake_list[0][1] == snake_list[i+3][1]:
            snake_speed = 0
            game_over = True

    # initial moving of the snake
    if not moving_down and not moving_up and not moving_left and not moving_right:
        for i in range(snake_length):
            snake_list[i][0] += snake_speed
            if snake_list[i][0] == W:
                snake_list[i][0] = 0
    # moving of the snake
    elif moving_down:
        change_coord(snake_list, snake_length)
        snake_list[0][1] = y_down(snake_list[0][1])
        if can_add_block_x_l(snake_list, snake_length) and food_eaten:
            snake_list.append([snake_list[snake_length - 1][0] - 20, snake_list[snake_length - 1][1]])
            snake_length += 1
            food_eaten = False
        elif can_add_block_x_r(snake_list, snake_length) and food_eaten:
            snake_list.append([snake_list[snake_length - 1][0] - 20, snake_list[snake_length - 1][1]])
            snake_length += 1
            food_eaten = False
    elif moving_up:
        change_coord(snake_list, snake_length)
        snake_list[0][1] = y_up(snake_list[0][1])
        if can_add_block_x_l(snake_list, snake_length) and food_eaten:
            snake_list.append([snake_list[snake_length - 1][0] - 20, snake_list[snake_length - 1][1]])
            snake_length += 1
            food_eaten = False
        elif can_add_block_x_r(snake_list, snake_length) and food_eaten:
            snake_list.append([snake_list[snake_length - 1][0] - 20, snake_list[snake_length - 1][1]])
            snake_length += 1
            food_eaten = False
    elif moving_right:
        change_coord(snake_list, snake_length)
        snake_list[0][0] = x_right(snake_list[0][0])
        if can_add_block_y_u(snake_list, snake_length) and food_eaten:
            snake_list.append([snake_list[snake_length - 1][0], snake_list[snake_length - 1][1] - 20])
            snake_length += 1
            food_eaten = False
        elif can_add_block_y_d(snake_list, snake_length) and food_eaten:
            snake_list.append([snake_list[snake_length - 1][0], snake_list[snake_length - 1][1] + 20])
            snake_length += 1
            food_eaten = False
    elif moving_left:
        change_coord(snake_list, snake_length)
        snake_list[0][0] = x_left(snake_list[0][0])
        if can_add_block_y_u(snake_list, snake_length) and food_eaten:
            snake_list.append([snake_list[snake_length - 1][0], snake_list[snake_length - 1][1] - 20])
            snake_length += 1
            food_eaten = False
        elif can_add_block_y_d(snake_list, snake_length) and food_eaten:
            snake_list.append([snake_list[snake_length - 1][0], snake_list[snake_length - 1][1] + 20])
            snake_length += 1
            food_eaten = False
    # moving through the edge of the screen
    if snake_list[0][0] == W:
        snake_list[0][0] = 0
    elif snake_list[0][0] == -20:
        snake_list[0][0] = W
    elif snake_list[0][1] == -20:
        snake_list[0][1] = H
    elif snake_list[0][1] == H:
        snake_list[0][1] = 0
    # filling color list
    for i in range(snake_length):
        #color_list.append((randint(0, 250), randint(0, 250), randint(0, 230)))
        #color_list.append(snake_color)
        color_list.append(choice(colors))
    # drawing the snake
    if not game_over:
        for i in range(snake_length):
            pg.draw.rect(screen, color_list[i], (snake_list[i][0], snake_list[i][1], 20, 20))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN and not moving_up:
                moving_down = True
                moving_up = False
                moving_right = False
                moving_left = False
            if event.key == pg.K_UP and not moving_down:
                moving_up = True
                moving_down = False
                moving_right = False
                moving_left = False
            if event.key == pg.K_RIGHT and not moving_left:
                moving_right = True
                moving_left = False
                moving_up = False
                moving_down = False
            if event.key == pg.K_LEFT and not moving_right:
                moving_left = True
                moving_right = False
                moving_up = False
                moving_down = False
            if event.key == pg.K_r and game_over:
                set_initial_parameters()

    pg.display.flip()

pg.quit()

