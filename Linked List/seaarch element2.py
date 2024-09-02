class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
def create_linked_list(elements):
    if not elements:
        return None
    
    head= Node(elements[0])
    current = head 

    for element in elements[1:]:
        current.next = Node(element)
        current = current.next

    return head

def search_linked_list(head, n):
    current = head
    index = 0
    found = False

    while current is not None:
        if current.data == n:
            print(f"Element found at position {index}")
            found = True
            break
        current = current.next
        index += 1

    if not found:
        print(f"Element {n} not found in the list.")

if __name__ == "__main__":
    # Input from the user
    elements = list(map(int, input("Enter the elements of the linked list separated by space: ").split()))
    n = int(input("Enter the element to search for: "))

    # Create linked list
    head = create_linked_list(elements)

    # Search for the element in the linked list
    search_linked_list(head, n)