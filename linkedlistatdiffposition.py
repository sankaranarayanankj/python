class Node:
    def __init__(self,node):
        self.node=node
        self.next=None
class List:
    def __init__(self):
        self.head=None
        
    def display(self):
        node1=self.head
        while(node1):
            print(node1.node)
            node1=node1.next
list1=List()
#Insert at node to the linked list
list1.head=Node(1)
list2=Node(2)
list1.head.next=list2
list3=Node(3)
list2.next=list3
list4=Node(5)
list3.next=list4
#Insert the node at beginning of the list
list5=Node(8)
list5.next=list1.head
list1.head=list5
#Insert the node at middle of the list
list6=Node(89)
list2.next=list6
list6.next=list3
#Insert the node at the end of the list
list7=Node(90)
list4.next=list7
list1.display()
#Delete the node at beginning of the list
list1.head=list2
#Delete the node at Middle of the list
list2.next=list4
#Delete the node at the last of the list
list4.next=None
