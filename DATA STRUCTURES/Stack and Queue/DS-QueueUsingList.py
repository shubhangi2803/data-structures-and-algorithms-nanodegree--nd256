class Queue:
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.size()==0:
            return None
        x=self.items[0]
        self.items=self.items[1:]
        return x
        #return self.storage.pop(0)

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
