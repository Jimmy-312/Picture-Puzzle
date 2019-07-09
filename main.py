import pygame
import puzzlepicture as pz
from pygame.locals import*


def end_win():
    font=pygame.font.Font(None,56)
    text=font.render("Awesome!",35,(255,0,0))
    textpos = text.get_rect(center=(screen[0]//2,screen[1]//2))
    return text,textpos

def main():
    print("Hello,Summer.")
    lines,files=3,'example.jpg'
    raw_group,sep,size=pz.load_image(files,lines)
    bricks,turn=pz.new_map(raw_group)

    pygame.init()
    DIS=pygame.display.set_mode(size)
 
    while True:
        DIS.fill((0,0,0))
        for i in bricks.bricks:
            img=i.img
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
        pygame.display.update()

if __name__=="__main__":
    main()