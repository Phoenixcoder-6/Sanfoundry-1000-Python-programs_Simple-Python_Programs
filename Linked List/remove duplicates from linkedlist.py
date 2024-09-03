class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

def create_nodes(head):
    current= head
    elements=[]
    while current:
        elements.append(current.data)
        current=current.next
    return elements

def remove_duplicates(head):
    elements= create_nodes(head)
    unique= set(elements)
    print("Unique elements in the linked list :", unique)

if __name__=="__main__":
    node1=Node(100)
    node2= Node(200)
    node3= Node(300)
    node4= Node(200)

    node1.next= node2
    node2.next=node3
    node3.next= node4

    head= node1

    remove_duplicates(head)
