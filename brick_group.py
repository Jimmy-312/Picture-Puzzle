class brick_group(object):
    def __init__(self):
        self.bricks=[]

    def add(self,brick):
        self.bricks.append(brick)

    def get_id(self):
        a={}
        for i in self.bricks:
            a[i.pos]=i.img[1]
        return a

    def get_pos(self):
        pos=[]
        for i in self.bricks:
            pos.append(i.pos)
        return pos
    
    def remove(self,pos):
        for i in self.bricks:
            if i.pos==pos:
                self.bricks.remove(i)

    def __getitem__(self,x):
        for i in self.bricks:
            if i.pos==x:
                return i
            if x==self.bricks.index(i):
                return i
    def __setitem__(self, key, value):
        import brick
        if key in self.get_pos():
            for i in self.bricks:
                if key==i.pos:
                    i.img=value
        else:
            self.add(brick.brick(value,key))

    def __eq__(self,other):
        pass

    def __len__(self):
        return len(self.bricks)
