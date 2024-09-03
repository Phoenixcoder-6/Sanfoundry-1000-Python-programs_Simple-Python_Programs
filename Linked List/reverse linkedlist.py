class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
def reverse_list(head):
    current=head
    prev= None    #tail of the reversed list

    while current is not None:
        next_node= current.next #it temporarily stores the next node in the list
        current.next= prev
        prev = current
        current= next_node

    head= prev
    return head

def print_linked_list(head):
    current= head
    while current is not None:
        print(current.data,end="->")
        current=current.next
    print("None")


node1= Node(1)
node2= Node(2)
node3= Node(3)
node4= Node(4)

node1.next=node2
node2.next=node3
node3.next= node4


print("Original linked list:")
print_linked_list(node1)

reversed_head= reverse_list(node1)

print_linked_list(reversed_head)




