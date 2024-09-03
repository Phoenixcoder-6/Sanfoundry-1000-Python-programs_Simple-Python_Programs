class node:
    def __init__(self,data):
        self.data= data
        self.next= None

node1= node(100)
node2= node(200)
node3= node(300)

node1.next= node2
node2.next= node3

head= node1
new_node= node(50)
new_node.next= head
head= new_node

while head is not None:
    print(head.data,end="->")
    head= head.next
print("None")
