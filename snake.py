#Source: https://gist.github.com/sanchitgangwar/2158089

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

[width,height] = [25,60]

curses.initscr()
win = curses.newwin(width, height, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT                                                    
score = 0

snake = [[4,10], [4,9], [4,8]]                                     
food = [10,20]                                                     

win.addch(food[0], food[1], 'o')                                   


   

REV_DIR_MAP = {
        KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
    }
	
while key != 27: 
                                                    
    win.border(0)
    win.timeout(200 - len(snake))   
    prevKey = key 	                                              
   
    event = win.getch()
    if event == -1:
        key=prevKey
    else:
        key=event 


    if key == ord(' '):                                            
        key = -1                                                   
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue
    
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     
        key = prevKey
		
    if key==REV_DIR_MAP[prevKey]:
	   key = prevKey
	   
    
	
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])
	   
    if snake[0][0] ==0:
        snake[0][0] = width-2    
    if snake[0][1] == 0:
        snake[0][1] = height-2
        
    if snake[0][0] == width:
        snake[0][0] = 1
    if snake[0][1] == height:
        snake[0][1] = 1

    if snake[0] in snake[1:]: break

    
    if snake[0] == food:                                            
        food = []
        score += 1
        while food == []:
            food = [randint(1, width-2), randint(1, height-2)]                
            if food in snake:
                food = []
        win.addch(food[0], food[1], 'o')
    else:
        last = snake.pop()                                          
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')
    
    
    
curses.endwin()
print("\nScore = " + str(score))
