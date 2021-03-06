from Point import Point
from Node import Node
from Rectangle import Rectangle

class KDtree:
    def __init__(self):
        self.root = None

    def insert(self, point):
        if (self.root == None):
            self.root = Node(None,None,point,0,None,0)
        else:
            self.root.add(point)

    def search(self, tl, br):
        rec = Rectangle(tl,br)
        if self.root == None:
            print("Empty tree")
        else:
            show = self.root.r_search(rec)
            for i in show:
                print(i.x,"|",i.y)
