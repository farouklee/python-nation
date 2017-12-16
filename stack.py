class stack:
    def __init__(self):
        self.stacker=[]

    def isempty(self):
        return self.stacker==[]

    def push(self, item):
        self.stacker.insert(0, item)

    def pop(self):
        return self.stacker.pop(0)

    def peek(self):
        return self.stacker[0]

    def size(self):
        return len(self.stacker)

import sys
#from stack import stack

def instructions():
    print('''Enter the following
            1 to push on the stack
            2 to pop from the stack
            3 to peek te stacl
            4 to check the size of stacck
            5 to end the process''')

stackobject= stack()
instructions()
choice= int(input("?"))

while choice !=5:
    if choice==1:
        stackobject.push(input('enter value: '))
        newstack=[]
        temp=vars(stackobject)
        for item in  temp:
            newstack.append(item)

            print ('The list is  {0}' .format(temp[item]))

    elif choice==2:
        pop=stackobject.pop()
        print (pop +' has been popped from the stack')
       # print(stackobject)
        temp =vars (stackobject)
        for item in temp:
            print (temp[item])

    elif choice==3:
        pop=stackobject.peek()
        print ('see? ' +pop)

    elif choice==4:
        pop=stackobject.size()
        print('the size of the stack is {0}' .format(pop))

    choice = int(input("?"))
