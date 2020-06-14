class Stack:
    def __init__(self):
        self.arr=[0]*10
        self.next_index=0
        self.num_elements=0

    def _handle_stack_capacity_full(self,data):
        old_arr=self.arr
        self.arr=[0]*(2*len(old_arr))
        for i in range(len(old_arr)):
            self.arr[i]=old_arr[i]
        self.push(data)

    def push(self, data):
        if len(self.arr)>self.next_index:
            self.arr[self.next_index] = data
            self.next_index += 1
            self.num_elements += 1
        else:
            self._handle_stack_capacity_full(data)

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        if self.num_elements==0:
            return True
        return False

    def pop(self):
        if self.is_empty():
            return None
        x=self.arr[self.next_index-1]
        self.next_index-=1
        self.num_elements-=1
        return x




foo = Stack()
print(foo.arr)
print("Pass" if foo.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] else "Fail")

foo = Stack()
foo.push("Test!")
print(foo.arr)
print("Pass" if foo.arr[0] == "Test!" else "Fail")

foo = Stack()
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(4)
foo.push(5)
foo.push(6)
foo.push(7)
foo.push(8)
foo.push(9)
foo.push(10) # The array is now at capacity!
foo.push(11) # This one should cause the array to increase in size
print(foo.arr) # Let's see what the array looks like now!
print("Pass" if len(foo.arr) == 20 else "Fail") # If we successfully doubled the array size, it should now be 20.

foo = Stack()
print(foo.size()) # Should return 0
print(foo.is_empty()) # Should return True
foo.push("Test") # Let's push an item onto the stack and check again
print(foo.size()) # Should return 1
print(foo.is_empty()) # Should return False

foo = Stack()
foo.push("Test") # We first have to push an item so that we'll have something to pop
print(foo.pop()) # Should return the popped item, which is "Test"
print(foo.pop()) # Should return None, since there's nothing left in the stack



class Stack:
    
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()
        
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element
    
    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

        
    
