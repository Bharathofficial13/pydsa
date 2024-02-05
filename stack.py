class stack:
    def __init__(self):
        self.items=[]
        
    def push(self,data):
        self.items.append(data)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
    def isempty(self):
        return len(self.items)==0
    def pri(self):
        print(self.items)

if __name__ =='__main__':
    s=stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.pop()
    s.pri()
    print(s.peek())
    s.isempty()
    