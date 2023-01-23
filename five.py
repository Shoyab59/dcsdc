# template
class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:
   def __init__(self):
       self.head = None
   def append(self, data):
       new_node = Node(data)
       if(self.head is None):
           self.head = new_node
           return 
       
       last_node = self.head
       while(last_node.next):
           last_node = last_node.next
       last_node.next = new_node

def find_middle( head ):
    if(head.next == None):
        return head.data

    slow = head 
    fast = head
    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next

    return slow