from pico2d import*
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
frame = 0
points_x = []
points_y = []
x = 100
y = 100
origin_x = 100
origin_y = 100
t = 0
i = 0
def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            points_x.append(event.x)
            points_y.append(TUK_HEIGHT - 1 - event.y)
def draw_hand():
    global hand_x, hand_y
    for i in range(0, len(points_x)):
        hand_arrow.draw(points_x[i],points_y[i])

def character_move():
    global x, y, origin_x, origin_y, t, i

    if len(points_x) == 0 and len(points_y) == 0:
        return

    t = i/100
    x = (1 - t) * origin_x + t * points_x[0]
    y = (1 - t) * origin_y + t * points_y[0]

    if x == points_x[0] and y == points_y[0]:
        origin_x = points_x.pop(0)
        origin_y = points_y.pop(0)
        i = 0
    i += 5


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    draw_hand()
    character_move()

    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    frame = (frame + 1) % 8

    update_canvas()
    delay(0.1)