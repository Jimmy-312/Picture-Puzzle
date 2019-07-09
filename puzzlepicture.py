from random import randint
from brick import brick
from brick_group import brick_group
def load_image(files,lines):
    from PIL import Image
    
    img=Image.open(files)
    x,y=img.size
    x1,y1=int(x/lines),int(y/lines)
    brick_list=brick_group()
    ID=0
    
    for i in range(lines):
        for j in range(lines):
            loc=(i*x1,j*y1,(i+1)*x1,(j+1)*y1)
            a=brick([img.crop(loc),ID],(i,j))
            brick_list.add(a)
            ID+=1

    num=randint(0,len(brick_list)-1)
    turn=brick_list[num].pos
    brick_list.remove(turn)
    
    return brick_list,(x1,y1),(x,y),turn

def get_loc(loc,size):
    return [loc[0]//size[0],loc[1]//size[1]]

def move(click_loc,turn,brick_list):
    a,b=click_loc[0],click_loc[1]
    x,y=turn[0],turn[1]
    if tuple(turn)==tuple(click_loc) or (a!=x and b!=y):return turn,brick_list
    if b==y:
        c,t,d=a,0,x  
    else:
        c,t,d=b,1,y
    m=abs(c-d)
    flag=repr(c-d)[0] if repr(c-d)[0]=='-' else '+'

    for i in range(m):
        d1=eval(str(d)+flag+str(i))
        d2=eval(str(d1)+flag+'1')
        p1,p2=[x,y],[x,y]
        p1[t],p2[t]=d1,d2
        p1,p2=tuple(p1),tuple(p2)
        brick_list[p1]=brick_list[p2].img
        
    turn=(a,b)
    brick_list.remove((a,b))
    return turn,brick_list

#be used to exam codes
'''def output(maps,lines):
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

def isfinish(img1,img2):
    if img1==img2:
        return True
    return False'''
