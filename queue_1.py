class queue:
    def __init__(self):
        self.items=[]
        
        
    def enque(self,data):
        self.items.append(data)
    def deq(self):
        self.items.pop(0)
    def peek(self):
        return self.items[0]
    def isempty(self):
        return len(self.items)==0
    def pri(self):
        print(self.items)

if __name__=='__main__':
    q=queue()
    q.enque(1)
    q.enque(2)
    q.enque(3)
    q.enque(4)
    q.deq()
    print(q.peek())
    q.pri()