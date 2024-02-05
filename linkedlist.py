class node:
    def __init__(self,data=None,nexts=None):
        self.data=data
        self.next=nexts
class linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_beg(self,data):
        if self.head==None:
            Node=node(data,self.head)
            self.head=Node
            return
        self.head=node(data,self.head)
        return
    def prints(self):
        if self.head is None:
            print("invalid")
            return
        itr=self.head
        l1=""
        while itr:
            l1+=str(itr.data)+"-->"
            itr=itr.next
            
        print(l1)
    def insert_at_end(self,data):
        if self.head==None:
            self.insert_at_beg(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node(data,None)
    def insert_val(self,data):
        self.head=None
        for x in data:
            self.insert_at_end(x)
        
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
    def insert_at_pos(self,data,index):
        if self.head==None:
            self.insert_at_beg
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                 Node=node(data,itr.next)
                 itr.next=Node
                 break
            itr=itr.next
            count+=1
    
    def del_beg(self):
        if self.head==None:
            print("empty")
            return
        self.head=self.head.next
    def del_end(self):
        if self.head==None:
            print("empty")
            return
        itr=self.head
        count=0
        index=self.get_length()-2
        
        while itr:
            if count==index:
                 itr.next=None
                
            itr=itr.next
            count+=1
    def del_all(self):
        self.head=None
        return
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
        itr=self.head
        count=0
        while itr:
            if count==index-2:
                itr.next=itr.next.next
            itr=itr.next
            count+=1
        
           
                
        
if __name__=='__main__' :
    ll=linkedlist()
  
    ll.insert_val([1,2,3,4,5])
    ll.insert_at_pos(4.5,4)
  
    ll.del_at_pos(1)
    ll.prints()

        