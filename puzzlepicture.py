from random import randint
from brick import brick
from brick_group import brick_group
def load_image(files,lines):
    from PIL import Image
    
    img=Image.open(files)
    x,y=img.size
    x1,y1=int(x/lines[1]),int(y/lines[0])
    brick_list=brick_group()
    ID=0
    
    for i in range(lines[1]):
        for j in range(lines[0]):
            loc=(i*x1,j*y1,(i+1)*x1,(j+1)*y1)
            a=brick([img.crop(loc),ID],(i,j))
            brick_list.add(a)
            ID+=1

    num=randint(0,len(brick_list)-1)
    turn=brick_list[num].pos
    brick_list.remove(turn)
    ans=brick_list.get_id()
    brick_list,turn,record=recreate_map(brick_list,turn,500)
    
    return brick_list,(x1,y1),(x,y),turn,ans,record

def recreate_map(bricks,turn,time):
    record_turn=[]
    for i in range(time):
        ch=get_choice(bricks,turn)
        num=randint(0,len(ch)-1)
        record_turn.append(turn)
        turn,bricks=move(ch[num],turn,bricks)
    return bricks,turn,record_turn

def fake_cheat(bricks,turn,record,mode):
    mode=True if record!=[] else False
    if not mode:return bricks,turn,record,mode
    turn,bricks=move(record[-1:][0],turn,bricks)
    record.pop()
    return bricks,turn,record,mode

def get_choice(bricks,t):
    choice=[(t[0]+1,t[1]),(t[0]-1,t[1]),(t[0],t[1]-1),(t[0],t[1]+1)]
    pos=bricks.get_pos()
    d=[]
    for i in choice:
        if i not in pos:
            d.append(i)
    for i in d:
        choice.remove(i)
    return choice

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
