import random
import curses
from curses import textpad

def create_food(worm, box):
    food = None
    while food is None:
        food = [random.randint(box[0][0]+1, box [1][0]-1), random.randint(box[0][1]+1, box [1][1]-1)]
        if food in worm:
            food = None
    return food

def print_score(stdscr, score):
    sh, sw = stdscr.getmaxyx()
    score_text = "Score: {}".format(score)
    stdscr.addstr(0, sw//2 - len(score_text)//2, score_text)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(350)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3, sw-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    stdscr.refresh()
    stdscr.getch()

    worm = [[sh//2, sw//2+1], [sh//2, sw//2], [sh//2, sw//2+1]]
    direction = curses.KEY_RIGHT

    for y,x in worm:
        stdscr.addstr(y, x, 'O')

    food = create_food(worm, box)
    stdscr.addstr(food[0], food[1], 'x')

    score = 0
    print_score(stdscr, score)

    while 1:
        key = stdscr.getch()
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

        head = worm[0]

        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        elif direction == curses.KEY_UP:
            new_head = [head[0]-1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0]+1, head[1]]

        worm.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], 'O')

        if worm[0] == food:
            food = create_food(worm, box)
            stdscr.addstr(food[0], food[1], 'o')

            score += 1
            print_score(stdscr, score)
        else:
            stdscr.addstr(worm[-1][0], worm[-1][1], ' ')
            worm.pop()

        if  (worm[0][0] in [box[0][0], box[1][0]] or
            worm[0][1] in [box[0][0], box[1][1]] or
            worm[0] in worm [1:]):
            msg = "Game Over!"
            stdscr.addstr(sh//2, sw//2 - len(msg)//2, msg)
            stdscr.nodelay(0)
            stdscr.getch()
            break

        stdscr.refresh()

curses.wrapper(main)