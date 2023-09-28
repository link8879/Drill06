from pico2d import*
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
hand_x, hand_y = 0, 0
points_x = []
points_y = []

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

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    draw_hand()
    update_canvas()
    delay(0.1)