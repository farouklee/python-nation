class node:

    def __init__(self,data):
        self.data= data
        self.nextnode= None

    def getdata(self):
        return self.data

    def setdata(self, data):
        self.data=data

    def getnextnode(self):
        return self.nextnode

    def setnextnode(self,newnode):
        self.nextnode=newnode

class list:
    def __init__(self):
        self.firstnode= None
        self.lastnode= None

    def isempty(self):
        return self.firstnode==None

    def add(self, item):
        temp= node(item)
        temp.setnextnode(self.firstnode)
        self.firstnode= temp

    def size(self,):
        current=self.firstnode
        count=0
        while current != None:
            count= count +1
            current=current.getnextnode()

        return count

    def search(self, item):
        current =self.firstnode
        found =False
        while current != None and not found:
            if current.getdata()==item:
                found =True
            else:
                current=current.getnextnode()
        return found

    def remove(self, item):
        current= self.firstnode
        previous=None
        found= False
        while not found:
            if current.getdata()==item:
                found= True
            else:
                previous =current
                current =current.getnextnode()

        if previous ==None:
            self.firstnode=current.getnextnode()
        else:
            previous.setnextnode(current.getnextnode())

    def popfirst(self):
        a=0
        current =self.firstnode

        previous= None
        found =False
        while not found:
            if current.getnextnode()==None:
                found =True
            else:
                previous=current
                current=current.getnextnode()

        if previous ==None:
            self.firstnode=current.getnextnode()
        else:
            previous.setnextnode(current.getnextnode())

        a=current.getdata()
        return a

    def indexer(self, x):
        count=0
        current= self.firstnode
        found= False
        while current!= None and not found:
            count=count+1
            if current.getdata()==x:
                found=True
            else:
                current=current.getnextnode()
        return count


mylist=list()
#mylist.add(32)
mylist.add(84)
mylist.add(12)
mylist.add(59)
mylist.add(25)
mylist.add(14)
mylist.add(121)
mylist.add(69)
mylist.add(235)
mylist.add(6)


#print(mylist.search(12))
print(mylist.search(141))

#mylist.add(141)
#print(mylist.search(141))
print(mylist.size())

mylist.remove(59)
#print('The size of the new list after the removal of 59 is {0}' .format(mylist.size()))

print(mylist.popfirst())
print(mylist.size())

print('The number 14 is on index {0}'   .format(mylist.indexer(14)))


#listers=[print(x) for x in mylist]
#listers
