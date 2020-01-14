from Point import Point
from Rectangle import Rectangle

class Node:
    def __init__(self,right,left,data,axis,parent,depth):
        self.right = None
        self.left = None
        self.data = data
        self.axis = axis
        self.parent = parent
        self.depth = depth
        
    def add(self,point):
        if(self.axis==0):
            if(point.x>self.data.x):
                if (self.right == None):
                    self.right = Node(None,None,point,self.axis+1,self,self.depth+1)
                else:
                    self.right.add(point)
            elif(point.x == self.data.x and point.y == self.data.y):
                raise Exception("Point already exists")
            else:
                if (self.left == None):
                    self.left = Node(None,None,point,self.axis+1,self,self.depth+1)
                else:
                    self.left.add(point)
        else:
            if(point.y>self.data.y):
                if (self.right == None):
                    self.right = Node(None,None,point,self.axis-1,self,self.depth+1)
                else:
                    self.right.add(point)
            elif(point.x == self.data.x and point.y == self.data.y):
                raise Exception("Point already exists")
            else:
                if (self.left == None):
                    self.left = Node(None,None,point,self.axis-1,self,self.depth+1)
                else:
                    self.left.add(point)

    def r_search(self,rec):
        if(self.axis==0):
            if (self.data.x < rec.tl.x) :
                if(self.right==None):
                    return rec.points
                return self.right.r_search(rec)
            if (self.data.x >rec.br.x) :
                if(self.left==None):
                    return rec.points
                return self.left.r_search(rec)
            if (self.data.x>=rec.tl.x and self.data.x<=rec.br.x):
                if(self.data.y<=rec.tl.y and self.data.y>=rec.br.y):
                    rec.points.append(self.data)
                    if self.right == None and self.left == None:
                        return rec.points
                
                if(self.right==None):
                    tmp = rec.points
                else:
                    tmp = self.right.r_search(rec)
                    for i in tmp:
                        if i not in rec.points:
                            rec.points.append(i)
                if(self.left==None):
                    return rec.points
                return self.left.r_search(rec)
        else:
            if(self.data.y>rec.tl.y):
                if(self.left==None):
                    return rec.points
                return self.left.r_search(rec)
            if(self.data.y<rec.br.y):
                if(self.right==None):
                    return rec.points
                return self.right.r_search(rec)
            if (self.data.y>=rec.br.y and self.data.y<=rec.tl.y):
                if(self.data.x>=rec.tl.x and self.data.x<=rec.br.x):
                    rec.points.append(self.data)
                    if self.right == None and self.left == None:
                        return rec.points
               
                if(self.right==None):
                    tmp = rec.points
                else:
                    tmp = self.right.r_search(rec)
                    for i in tmp:
                        if i not in rec.points:
                            rec.points.append(i)
                if(self.left==None):
                    return rec.points
                return self.left.r_search(rec)
        

            
                
        
        
