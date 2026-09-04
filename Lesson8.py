import pgzrun
from random import randint 
from time import time

WIDTH = 800
HEIGHT = 600

stars = []
lines = []
next_star = 0

start_time = 0
time_left = 15

number_of_stars =7
game_over = False

def create_stars():
    global start_time, stars, lines, next_star, time_left, game_over
    
    stars = []
    lines = []
    next_star = 0
    time_left = 15
    game_over = False
    
    for i in range(number_of_stars):
        star = Actor("star")
        star.pos = randint(60, WIDTH-60), randint(60, HEIGHT-60)
        stars.append(star)
        
    start_time = time()

def update():
    global time_left, game_over
    if not game_over and next_star < number_of_stars:
        time_left = 15 - int(time() - start_time)
        
        if time_left <= 0:
            time_left = 0
            game_over = True

def draw(): 
    screen.blit("background", (0,0))
    number = 1

    for star in stars:
        star.draw()
    
        screen.draw.text(
            str(number),
            center=(star.x,star.y + 40),
            fontsize=35,
            color="white",
            owidth=1.5,
            ocolor="black"
        )
    
        number += 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 150))
        
    if next_star < number_of_stars:
        total_time = time() - start_time
        
    screen.draw.text(
        "Time:" +str(time_left),
        (10,10),
        fontsize=40,
        color="cyan",
        owidth=1.5,
        ocolor="black"
    )
    
    if next_star == number_of_stars and not game_over:
        screen.draw.text(
            "Constellation Completed!",
            center = (WIDTH / 2, 50),
            fontsize=50,
            color="yellow",
            owidth=1.5,
            ocolor="black"
        )
        
    if game_over:
        screen.draw.text(
            "GAME OVER!",
            center = (WIDTH / 2, HEIGHT / 2 - 30),
            fontsize = 70,
            color = "red",
            owidth = 2,
            ocolor = "black"
        )
        
        screen.draw.text(
            "Click to Restart",
            center = (WIDTH / 2, HEIGHT / 2 + 50),
            fontsize = 35,
            color = "white",
            owidth = 1.5,
            ocolor = "black"
        )
        
def on_mouse_down(pos):
    global next_star
    
    if game_over:
        create_stars()
        return
    
    if next_star < number_of_stars:
        
        if stars[next_star].collidepoint(pos):
            if next_star > 0:
                lines.append(
                    (stars[next_star - 1].pos, stars[next_star].pos)
                )
                
            next_star += 1
                
    else:
        create_stars()
create_stars()
pgzrun.go()