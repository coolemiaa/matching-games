import pygame
pygame.init() #initialiation, provisdes, values
screen=pygame.display.set_mode((600,600)) #grootte van scherm
screen.fill('blue')
pygame.display.update()

subwaysurfer=pygame.image.load('matchingwordsgame/subwaysurfers.png')
ludo=pygame.image.load('matchingwordsgame/ludo.png')
templerun=pygame.image.load('matchingwordsgame/templerun.png')
candycrush=pygame.image.load('matchingwordsgame/candycrush.jpg')
screen.blit(subwaysurfer,(100,50))
screen.blit(ludo,(100,200))
screen.blit(templerun,(100,350))
screen.blit(candycrush,(100,500))

font=pygame.font.SysFont('Times New Roman',36)
text=font.render('ludo',True,'pink')
screen.blit(text,(350,75))

text2=font.render('subwaysurfers',True,'pink')
screen.blit(text2,(350,525))

text3=font.render('templerun',True,'pink')
screen.blit(text3,(350,225))

text4=font.render('candycrush',True,'pink')
screen.blit(text4,(350,375))







pygame.display.update()
run=True #zodat het scherm blijft en quit=false als je sluit sluit het
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False

        if i.type==pygame.MOUSEBUTTONDOWN: #event is mousebuttondown altijd in hoofdletter, drm doe je i.type dat is de i van for loop.
            pos=pygame.mouse.get_pos() #pos where mouse was pressed
            pygame.draw.circle(screen,'black',pos,10,0)
            pygame.display.update()


        elif i.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            pygame.draw.line(screen,'black',pos,pos2,5)
            pygame.draw.circle(screen,'black',pos2,10,0)
            pygame.display.update()
            

