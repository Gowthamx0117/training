class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

def create_linked_list(values):
    head=None
    for value in reversed(values):
        new_node=Node(value)
        new_node.next=head
        head=new_node
    return head

def print_linked_list(head):
    curr=head
    while curr:
        print(curr.data,end=" -> " if curr.next else "\n")
        curr=curr.next

