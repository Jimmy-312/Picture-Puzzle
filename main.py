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

def enter_game(DIS):
    f=True
    DIS.fill((0,0,0))
    font=pygame.font.Font(None,56)
    font2=pygame.font.Font(None,40)
    text=font.render("Puzzle Picture",0,(255,255,255))
    text2=font2.render("Select Image",0,(0,0,0))
    textpos = text.get_rect(center=(250,70))
    files=''
    while f:
        DIS.blit(text,textpos)
        pygame.draw.rect(DIS,(255,255,255),(150,150,200,50))
        DIS.blit(text2,(163,162))
        for event in pygame.event.get():
            if event.type==QUIT:
                return False
            if event.type==MOUSEBUTTONDOWN:
                arrow=pygame.mouse.get_pressed()
                pos=pygame.mouse.get_pos()
                button=arrow[0]
                if button==1 and 150<=pos[0]<=350 and 150<=pos[1]<=200:
                    files=select_file()
            if files!='':f=False
            pygame.display.update()
    return files

def select_file():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def main():
    print("Hello,Summer.")
    lines=(8,6)
    fix_mode=False

    pygame.init()
    DIS=pygame.display.set_caption("Puzzle Picture")
    DIS=pygame.display.set_mode((500,300))
    files=enter_game(DIS)
    if not files:return

    bricks,sep,size,turn,ans,record=pz.load_image(files,lines)
    DIS=pygame.display.set_mode(size)
    COUNT=USEREVENT+1
    pygame.time.set_timer(COUNT,100)

    while True:
        DIS.fill((255,255,255))
        for i in bricks:
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
                record.append(turn)
            elif event.type==KEYDOWN:
                if event.key==K_f:
                    fix_mode=not fix_mode
            elif event.type==COUNT and fix_mode:
                bricks,turn,record,fix_mode=pz.fake_cheat(bricks,turn,record,fix_mode)
        end_win(bricks.get_id(),ans,size,DIS)
        pygame.display.update()

if __name__=="__main__":
    main()