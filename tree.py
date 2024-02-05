class tree:
    def __init__(self,data=None):
        self.data=data
        self.item=[]
        self.parent=None
    def add_child(self,data):
        data.parent=self
        self.item.append(data)
    def prints(self):
        spaces=' '*self.get_lev()*3
        print(spaces,"|__",self.data)
        
        for i in self.item:
            i.prints()
    def get_lev(self):
        level=0
        p=self.parent
        while p:
            level+=1 
            p=p.parent
        return level


def treebu():
    root=tree("Electronics")
    root1=tree("washing")
    root2=tree("tv")
    lap=tree("lap")
    mach=tree("washing ma")
    lg=tree("lg")
    root.add_child(lap)
    root1.add_child(mach)
    root2.add_child(lg)
   
    root.prints()
    root1.prints()
    root2.prints()
    print(lap.get_lev())
if __name__=='__main__':
    treebu()