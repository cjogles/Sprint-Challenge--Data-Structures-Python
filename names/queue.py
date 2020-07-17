"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your stack class to implement the Queue?
         What would that look like? How many stacks would you need? Try it!
"""
from node import Node
from node import LinkedList

# ARRAY IMPLEMENTATION
# class Queue:
#     def __init__(self):
#         self.queue = []

#     def __len__(self):
#         return len(self.queue)

#     def enqueue(self, value):
#         self.queue.append(value)

#     def dequeue(self):
#         if self.queue.__len__() == 0:
#             pass
#         else:
#             value = self.queue[0]
#             self.queue.pop(0)
#             return value

# LINKED LIST IMPLEMENTATION


class Queue:
    def __init__(self):
        self.size = 0
        self.queue = LinkedList()

    def __repr__(self):
        return (f"queue: {self.queue}, size: {self.size}")

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.queue.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            pass
        else:
            self.size -= 1
            return self.queue.remove_head()

# jackson = Queue();
# jackson.enqueue("1")
# jackson.enqueue(21)
# print(jackson.__len__())
