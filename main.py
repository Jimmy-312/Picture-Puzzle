from random import randint
def load_image(files,lines):
    from PIL import Image
    global img_dict
    
    img=Image.open(files)
    x,y=img.size
    x1,y1=int(x/lines),int(y/lines)
    loc_list=[]
    
    for i in range(lines):
        for j in range(lines):
            loc=(i*x1,j*y1,(i+1)*x1,(j+1)*y1)
            loc_list.append([loc,(i,j)])
    img_dict={loc[1]:img.crop(loc[0]) for loc in loc_list}
    
    return img_dict,(x1,y1),(x,y)

def new_map(img_dict):
    num=randint(0,len(img_dict.keys()))
    loc_list=list(img_dict.keys())
    turn=loc_list.pop(num)
    img_dict.pop(turn)

    return loc_list,turn

    a=list(img_dict.keys())
    b=list(img_dict.values())

def get_loc(loc,size):
    return [loc[0]//size[0],loc[1]//size[1]]

def move(click_loc,maps,turn,img_dict):
    a,b=click_loc[0],click_loc[1]
    x,y=turn[0],turn[1]
    if turn==click_loc or (a!=x and b!=y):return maps,turn,img_dict
    c=a if b==y else b
    d=x if b==y else y
    maps.remove((a,b))
    maps.append((x,y))
    m=abs(c-d)
    flag=repr(d-b)[0] if repr(d-b)[0]=='-' else '+'
    for i in range(m):
        d1=eval(str(d)+flag+str(i))
        d2=eval(str(d1)+flag+'1')
        p1,p2=[x,y],[x,y]
        p1[int('0.5'+flag+'0.5')],p2[int('0.5'+flag+'0.5')]=d1,d2
        p1,p2=tuple(p1),tuple(p2)
        e=img_dict[p1]
        img_dict[p1]=img_dict[p2]
        img_dict[p2]=e
    turn=(a,b)
    #print((a,b))
    return maps,turn,img_dict

def output(maps,lines):#be used to exam codes
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

def isfinish(DIS,screen):
    global r_img,img_dict
    if r_img==img_dict:
        return True
    return False
