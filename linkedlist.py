class Node:
    def __init__(self,node=0):
        self.node=node
        self.next=None
class List:
    def __init__(self):
        self.head=None
list1=List()
list1.head=Node(3)
second=Node(2)
list1.head.next=second
third=Node(6)
third.next=second.next
second.next=third
fourth=Node(8)
fourth.next=second.next
third.next=fourth.next
second.next=fourth

    
