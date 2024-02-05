class node:
    def __init__(self,prev=None,data=None,nexts=None):
        self.prev=prev
        self.data=data
        self.next=nexts
class linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_beg(self,data):
        if self.head==None:
            Node=node(None,data,self.head)
            self.head=Node
            return
        
        Node = node(None, data, self.head)
        self.head.prev = Node  # Update the prev attribute of the existing head node
        self.head = Node
    def prints_forward(self):
        if self.head is None:
            print("invalid")
            return
        itr=self.head
        l1=""
        while itr:
            l1+=str(itr.data)+"-->"
            itr=itr.next
            
        print(l1)
    def prints_back(self):
        if self.head is None:
            print("invalid")
            return
        
        itr=self.head
        l1=""
        while itr.next:
            itr=itr.next
        while itr:
            l1+=str(itr.data)+"-->"
            itr=itr.prev
        print(l1)
   
    def insert_at_end(self,data):
        if self.head==None:
            self.insert_at_beg(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        Node=node(itr,data,None)
        itr.next=Node
    
    def insert_at_pos(self,data,index):
        if self.head==None:
            self.insert_at_beg
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                 Node=node(itr.prev.next,data,itr.next)
                 itr.next.prev=Node 
                 itr.next=Node
                 break
            itr=itr.next
            count+=1  
        
    def del_beg(self):
          if self.head==None:
            print("emp")
            return
          self.head=self.head.next
    
    def del_end(self):
        if self.head==None:
            print("emp")
            return
        itr=self.head
        count=0
        index=self.get_length()-2
        
        while itr:
            if count==index:
                 itr.next=None
                
            itr=itr.next
            count+=1  
        
    def get_length(self):
        if self.head==None:
            print("emptu")
            return
        itr=self.head
        count=0;
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def del_at_pos(self,index):
        if self.head==None:
            print("emp")
            return
        if self.get_length()==1:
            self.del_all()
            return
        if index==1:
            self.del_beg()
            return
        if index==self.get_length():
            self.del_end()
            return
        itr=self.head
        count=0
        while itr:
            if count==index-2:
                itr.next=itr.next.next
                itr.prev=itr.next.prev
            itr=itr.next
            count+=1
        
    def del_all(self):
        self.head=None
        return
if __name__=='__main__' :
    ll=linkedlist()
  
    ll.insert_at_beg(1)
    ll.insert_at_beg(2)
    ll.insert_at_beg(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_at_pos(2.5,2)
   
    ll.del_at_pos(6)
    ll.prints_forward()

        