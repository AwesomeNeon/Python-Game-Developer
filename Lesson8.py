import pgzrun
from random import randint 
from time import time

WIDTH = 800
HEIGHT = 600

stars = []
lines = []
next_star = 0

start_time = 0
total_time = 0

number_of_stars = 7

def create_stars():
    global start_time, stars, lines, next_star
    
    stars = []
    lines = []
    next_star = 0
    
    for i in range(number_of_stars):
        star = Actor("star")
        star.pos = randint(60, WIDTH-60), randint(60, HEIGHT-60)
        stars.append(star)
        
        start_time = time()
def draw(): global total_time

screen.blit("background", (0,0))
number = 1

for star in stars:
    star.draw()
    
    screen.draw.text(
        str(number),
        center=(star.x,star.y + 40),
        fontsize=35
        color"white"
        owidth=1.5,
        ocolor="black"
    )
    
    number += 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 150))
        
        if next_star < number_of_stars:
            total_time = time - start_time