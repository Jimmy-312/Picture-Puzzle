import pygame
import puzzlepicture as pz
from pygame.locals import*
from copy import deepcopy

def end_win(img1,img2,size,DIS):
    if not img1==img2:return
    font=pygame.font.Font(None,56)
    text=font.render("Awesome!",35,(255,0,0))
    textpos = text.get_rect(center=(size[0]//2,size[1]//2))
    DIS.blit(text,textpos)

def main():
    print("Hello,Summer.")
    lines,files=3,'example.jpg'
    bricks,sep,size,turn=pz.load_image(files,lines)
    ans=bricks.get_id()

    pygame.init()
    DIS=pygame.display.set_mode(size)
 
    while True:
        DIS.fill((0,0,0))
        for i in bricks.bricks:
            img=i.img[0]
            pos=i.pos
            _image = pygame.image.fromstring(img.tobytes(),img.size,img.mode) 
            DIS.blit(_image,(sep[0]*pos[0],sep[1]*pos[1]))
        for event in pygame.event.get():
            if event.type==QUIT:
                return
            elif event.type==MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                pos=pz.get_loc((x,y),sep)
                turn,bricks=pz.move(pos,turn,bricks)
        end_win(bricks.get_id(),ans,size,DIS)
        pygame.display.update()

if __name__=="__main__":
    main()