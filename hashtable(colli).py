class hashtable:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]
    
    def get_hash(self,data):
        h=0 
        for char in data:
            h+=ord(char)
        return h%self.MAX 
        
    def __getitem__(self,key):
        h=self.get_hash(key)
        for ele in (self.arr[h]):
            if ele[0]==key:
                return ele[1]
        
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found =False
        for idx,ele in enumerate(self.arr[h]):
            if ele[0]==key:
                self.arr[h][idx]==(key,val)
                found=True
                break
        if not found:
            self.arr[h].append((key,val))

if __name__=='__main__':
    t=hashtable()
    t.__setitem__('march 6',20)
    t.__setitem__('march 17',40)
    print(t['march 6'])
        