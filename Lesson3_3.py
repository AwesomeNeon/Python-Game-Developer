import pgzrun
WIDTH = 800
HEIGHT = 550
def draw():
    screen.fill((0,0,0))
    
    screen.draw.text("NEON WIREFRAME CITY", center=(500, 50), fontsize=55,color=(255,0,255))
    
    
    
    sun_x = 500
    sun_y = 180 
    radius = 90
    
    screen.draw.circle((sun_x,sun_y),radius,(255,0,255))
    
    for y in range (130,240,15):
        screen.drawline((420,y),(580,y),(255,0,255))
        
        horizon_y = 420
        screen.draw.line((0,horizon_y),(1000, horizon_y),(0,255,255))
        vanish_x =500
        vanish_y = horizon_y
        
        for x in range(0,1001,40):
            screen.draw.line((x,HEIGHT),(vanish_x,vanish_y,)(0,255,255))
           
            y = horizon_y + 20
            gap = 20
            
            while y < HEIGHT:
                screen.draw.line((0,y),(1000,y),(0,255,255))
                y += ga
                gap +=6
                
                left_bulidings = [(50,220,70,200),(150,170,90,250),(280,270,60,150)]
                
                for x, y, w, h in left_bulidings
                
                offset = 30
                screen.draw.rect(Rect((x,y),(w,h)), (255,0,255))
                
                screen.draw.line((x,y), (x + offset,y - offset),(255,0255,255))
                screen.draw.line((x + w,y)(x+w+offset, y - offset ),(255,0,255))
                screen.draw.line(
                    (x + w, y + h),( x + w + offset),(255,0,255)
                )