class node:
    def __init__(self,data):
        self.data= data
        self.next= None

node1= node(100)
node2= node(200)
node3= node(300)

node1.next= node2
node2.next= node3

head=node1
n=300
current = head
index=0
found= False
while current is not None:
    if (current.data==n):
        print(f"Element found at position {index}")
        found =True
        break
    current = current.next
    index +=1
#print("None")   

if not found:
    print(f"Element {n} not found in the list.")