# Helper Code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    current_node=linked_list.head
    size=0
    while current_node is not None:
        size+=1
        current_node=current_node.next

    #print("Size calculated {}".format(size))
        
    new_list=LinkedList()
    current=new_list.head        
    current_node=linked_list.head
    count=0
    while count<size:
        #print('count = {}  '.format(count),end='  ')
        #print('value = {}'.format(current_node.value))
        new_list.append(current_node.value)        
        current_node=current_node.next
        count+=1

    #print("New list created ")
    #print(list(new_list))

    p=new_list.head
    q=None
    r=None
    while p:
        r=q
        q=p
        p=p.next
        q.next=r
    new_list.head=q
    
    return(new_list)

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)
    
#print(list(llist))
flipped = reverse(llist)

#print(list(llist))
#print(list(flipped))

is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
