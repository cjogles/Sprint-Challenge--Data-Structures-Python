class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

# I am assuming that node is always the head of linked list, and prev is always None (the params)
# this is a poor method for a public class because node and prev could be anything. It would be hard to use, good
# for a private method because its easy to write the function. 
# started with the base case that as long as my node is not equal to none, then I have work to do. otherwise, my node
# is the new head. 
    def reverse_list(self, node, prev): 
        if node == None:
            self.head = prev
        else:
            next_node = node.next_node
            node.next_node = prev
            self.reverse_list(next_node, node)
        
        



            
