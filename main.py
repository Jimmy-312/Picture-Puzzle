import pygame
from pygame.locals import*
from random import randint
def load_image(files,lines):
    from PIL import Image

    img=Image.open(files)
    x,y=img.size
    x1,y1=int(x/lines),int(y/lines)
    loc_list=[]
    for i in range(lines):
        for j in range(lines):
            loc=(i*x1,j*y1,(i+1)*x1,(j+1)*y1)
            loc_list.append([loc,(i,j)])
    img_dict={loc[1]:img.crop(loc[0]) for loc in loc_list}
    a=list(img_dict.keys())
    b=list(img_dict.values())
    _img={}
    for i in a:
        _img[i]=b[randint(0,len(b)-1)]
        b.remove(_img[i])
    return img_dict,_img,(x1,y1),(x,y)

def new_map():
    from random import sample
    global img_list
    #raw=sample(range(len(right_map),len(right_map)-1))
    #maps=[right_map(i) for i in raw]
    maps=list(img_list.keys())[:-1]
    turn=set(img_list.keys()).difference(set(maps))
    return maps,list(turn)[0]

def move(loc,size):
    global maps,turn,img_list
    click_loc=[loc[0]//size[0],loc[1]//size[1]]
    a,b=click_loc[0],click_loc[1]
    x,y=turn[0],turn[1]
    if x==a and b!=y:
        maps.remove((a,b))
        maps.append((x,y))
        m=max(b,y)-min(b,y)
        if b<y:
            for i in range(m):
                d=img_list[(x,y-i)]
                img_list[(x,y-i)]=img_list[(x,y-(i+1))]
                img_list[(x,y-(i+1))]=d
        if b>y:
            for i in range(m):
                d=img_list[(x,y+i)]
                img_list[(x,y+i)]=img_list[(x,y+(i+1))]
                img_list[(x,y+(i+1))]=d
        turn=(a,b)
    elif x!=a and y==b:
        maps.remove((a,b))
        maps.append((x,y))
        m=max(a,x)-min(a,x)
        if a<x:
            for i in range(m):
                d=img_list[(x-i,y)]
                img_list[(x-i,y)]=img_list[(x-(i+1),y)]
                img_list[(x-(i+1),y)]=d
        if a>x:
            for i in range(m):
                d=img_list[(x+i,y)]
                img_list[(x+i,y)]=img_list[(x+(i+1),y)]
                img_list[(x+(i+1),y)]=d
        turn=(a,b)
    print((a,b))
    return maps

def output(maps,lines):
    out=[]
    for i in range(lines):
        out.append([])
        for j in range(lines):
            out[i].append([])
    for i in range(lines):
        for j in range(lines):
            out[j][i]='-'
    for i in maps:
        out[i[1]][i[0]]='*'
    for i in out:
        print(i)

def show(lines,DIS,size):
    global img_list,maps
    for i in maps:
        im=img_list[i]
        _image = pygame.image.fromstring(im.tobytes(),im.size,im.mode) 
        DIS.blit(_image,(size[0]*(i[0]),size[1]*(i[1])))

def isfinish(DIS,screen):
    global r_img,img_list
    if r_img==img_list:
        font=pygame.font.Font(None,56)
        text=font.render("Awesome!",35,(255,0,0))
        textpos = text.get_rect(center=(screen[0]//2,screen[1]//2))
        DIS.blit(text,textpos)

def main():
    print("Hello,Summer.")
    global maps,turn,img_list,r_img
    lines=3
    files='C://Users//12806//Desktop//Summer Idea//img.jpg'
    r_img,img_list,size,screen=load_image(files,lines)
    maps,turn=new_map()


    pygame.init()
    DIS=pygame.display.set_mode(screen)
    #print(turn)
    show(lines,DIS,size)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                return
            elif event.type==MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                move((x,y),size)
                DIS.fill((0,0,0))
                show(lines,DIS,size)
                output(maps,lines)
        isfinish(DIS,screen)        
        pygame.display.update()


if __name__=="__main__":
    main()
