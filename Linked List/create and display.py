class node:
    def __init__(self,data):
        self.data=data
        self.next= None

node1=node(100)
node2=node(200)
node3=node(300)

node1.next=node2
node2.next=node3

current=node1
while current is not None:
    print(current.data,end="->")
    current= current.next
print("None")
