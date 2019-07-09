import pygame
from pygame.locals import*

def show(size):
    for i in maps:
        im=img_dict[i]
        _image = pygame.image.fromstring(im.tobytes(),im.size,im.mode) 
        return image,(size[0]*(i[0]),size[1]*(i[1])))

def end_win():
    font=pygame.font.Font(None,56)
    text=font.render("Awesome!",35,(255,0,0))
    textpos = text.get_rect(center=(screen[0]//2,screen[1]//2))
    return text,textpos

def main():
    print("Hello,Summer.")
    lines=3
    files='example.jpg'
    r_img,size,screen=load_image(files,lines)
    maps,turn=new_map(img_dict)


    pygame.init()
    DIS=pygame.display.set_mode(screen)
    #print(turn)
    show(DIS,size)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                return
            elif event.type==MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                pos=get_loc((x,y))
                maps,turn,img_dict=move(pos,maps,turn,img_dict)
                
                DIS.fill((0,0,0))
                show(lines,DIS,size)
                output(maps,lines)
        #isfinish(DIS,screen)        
        pygame.display.update()

if __name__=="__main__":
    main()