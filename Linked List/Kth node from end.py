class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def check(head, k):
    slow = fast = head

    # Move the fast pointer k steps ahead
    for _ in range(k):
        if fast is None:
            return -1  # k is larger than the length of the list
        fast = fast.next

    # Move both fast and slow pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    return slow.data if slow else -1  # Return the data of the k-th node from the end

def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0].strip())  # Number of test cases
    idx = 1

    while t > 0:
        # Read linked list elements and k value from user input
        arr = list(map(int, data[idx].strip().split()))
        k = int(data[idx + 1].strip())
        idx += 2
        
        # Create linked list from input
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        # Call the check function to find the k-th node from the end
        result = check(head, k)
        print("The data of the k-th node from the end is:", result)
        
        t -= 1
