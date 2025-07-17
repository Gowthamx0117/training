class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(values):
    head = None
    for value in reversed(values):
        new_node = Node(value)
        new_node.next = head
        head = new_node
    return head

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next

def sort_linked_list(head):
    # Step 1: Extract values
    values = []
    curr = head
    while curr:
        values.append(curr.data)
        curr = curr.next
    
    # Step 2: Sort values
    values.sort()

    # Step 3: Create new linked list from sorted values
    return create_linked_list(values)

if __name__ == "__main__":
    values = list(map(int, input("Enter elements: ").split()))
    head = create_linked_list(values)
    
    print("Original Linked List:")
    print_linked_list(head)
    
    head = sort_linked_list(head)
    
    print("Sorted Linked List:")
    print_linked_list(head)
