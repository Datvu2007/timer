import pygame
from datetime import datetime
from math import sin,cos,pi

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((280, 300))
pygame.display.set_caption('Timer')

font = pygame.font.SysFont('arial', 25)
font1 = pygame.font.SysFont('arial', 40)

start_text = font.render('Start', False, (0,0,0))
stop_text  = font.render('Stop' , False, (0,0,0))
reset_text = font.render('Reset', False, (0,0,0))

def get_text_time(d,h,m,s):
    time=[str(d),str(h),str(m),str(s)]
    for i in range(len(time)):
        if len(time[i])==1:
            time[i]='0'+time[i]
    return ' : '.join(time)
def getxy(n,a):
    while a>=360:a-=360
    if a==0:return[0,n]
    elif a==90:return[n,0]
    elif a==180:return[0,-n]
    elif a==270:return[-n,0]
    elif 0<a<90:return[sin(a)*n,cos(a)*n]
    elif 90<a<180:return[cos(a-90)*n,sin(a-90)*n]
    elif 180<a<270:return[-sin(a-180)*n,-cos(a-180)*n]
    else:return[-cos(a-270)*n,sin(a-270)*n]

running=True

h=0
m=0
s=0
msc10=0

xs=0
ys=85
xm=0
ym=70
xh=0
yh=50

start=False

while running:
    pygame.time.Clock().tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            print(mx,my)
            if  250<=my<=290:
                if 55<=mx<=135 and not start:
                    start=True
                elif 55<=mx<=222 and start:
                    start=False
                elif 142<=mx<=222 and not start:
                    h=0
                    m=0
                    s=0
                    msc10=0

    screen.fill((150,150,150))
    if start:
        msc10+=1
        if msc10>99:
            msc10=0
            s+=1
        if s>59:
            s=0
            m+=1
        if m>59:
            h+=1
    xs,ys=getxy(85,(360/60)*s*pi/180)
    xm,ym=getxy(70,(360/60)*m*pi/180)
    xh,yh=getxy(50,(360/12)*h*pi/180)
    #draw time
    screen.blit(font1.render(get_text_time(h,m,s,msc10),False,(255,255,255)),(2,0))

    #draw clock
    pygame.draw.circle(screen, (0,0,0), (140, 140), 100)
    pygame.draw.circle(screen, (255,255,255), (140, 140), 95)
    for i in range(12):
        tx,ty=getxy(91,(360/12)*i*pi/180)
        pygame.draw.circle(screen, (0,0,0), (140+tx, 140-ty), 3)
    #draw hand
    pygame.draw.line(screen, (150,150,150), (140, 140), (140+xs, 140-ys), 2)
    pygame.draw.line(screen, (0,0,0), (140, 140), (140+xm, 140-ym), 4)
    pygame.draw.line(screen, (255,0,0), (140, 140), (140+xh, 140-yh), 4)
    #draw dot
    pygame.draw.circle(screen, (100,100,100), (141, 140), 5)

    if start:
        #draw stop button
        pygame.draw.rect(screen, (255,0,0), (55, 250, 167, 40))
        screen.blit(stop_text,(112,253))
    else:
        #draw start button
        pygame.draw.rect(screen, (0,255,0), (55, 250, 80, 40))
        screen.blit(start_text,(67 ,253))
        #draw reset button
        pygame.draw.rect(screen, (255,0,0), (142, 250, 80, 40))
        screen.blit(reset_text  ,(147 ,253))

    pygame.display.update()
pygame.quit()