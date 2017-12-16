class node:
    def __init__(self, val):
        self.value=val
        self.leftchild= None
        self.rightchild= None

    def insert(self, data):
        if self.value==data:
            return  False
        elif self.value >data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild=node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild=node(data)
                return  True

    def find(self, data):
        if (self.value==data):
            return True
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftchild:
                self.leftchild.postorder()
            if self.rightchild:
                self.rightchild.postorder()

    def postorder(self):
        if self:
            if self.leftchild:
                self.leftchild.preorder()
            if self.rightchild:
                self.rightchild.preorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftchild:
                self.leftchild.inorder()
            print(str(self.value))
            if self.rightchild:
                self.rightchild.inorder()



class Tree:
    def __int__(self):
        self.root= None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root=node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False


    def preorder(self):
        print("Preorder")
        self.root.preorder()

    def postorder(self):
        print("Postorder")
        self.root.postorder()

    def inorder(self):
        print("inorder")
        self.root.inorder()


bst= Tree()
bst.insert(10)
print(bst.insert(15))
bst.preorder()
bst.postorder()