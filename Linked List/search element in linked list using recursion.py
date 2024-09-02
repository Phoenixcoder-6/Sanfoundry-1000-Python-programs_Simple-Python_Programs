class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def search_element(head,n,index=0):
    if head is None:
        return -1
    elif head.data == n:
        return index
    return search_element(head.next,n,index+1)
if __name__=='__main__':
    node1= node(100)
    node2= node(300)
    node3 = node(400)

    node1.next= node2
    node2.next= node3

    head= node1
    current= head
    n=300

    result= search_element(current,n)
    if result != -1:
        print(f"Element {n} found at position {result}")
    else:
        print(f"Element {n} not found in the list.")



