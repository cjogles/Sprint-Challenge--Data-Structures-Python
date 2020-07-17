from queue import Queue
from stack import Stack
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # case1 value is less then self.value
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            elif self.left == self.value:
                pass
            else:
                self.left.insert(value)

        # case2 value is greater then or equal to self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            elif self.right == self.value:
                pass
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass
        # case1 if self.value is equal to target
        if self.value == target:
            return True
        # case2 if target is less then self.value:
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # case3 if target is greater then or equal to self.value:
        if target >= self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # version1
        # current_node = self
        # while (current_node.right):
        #     current_node = current_node.right
        # return current_node.value
        # version2
        if self.right != None:
            return self.right.get_max()
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

# Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self is None:
            return
        if self.left is not None:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        line = Queue()
        line.enqueue(node)
        while line.__len__() > 0:
            my_value = line.dequeue()
            print(my_value.value)
            if my_value.left:
                line.enqueue(my_value.left)
            if my_value.right:
                line.enqueue(my_value.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        stack = Stack()
        stack.push(node)
        while stack.__len__() > 0:
            my_value = stack.pop()
            print(my_value.value)
            if my_value.right:
                stack.push(my_value.right)
            if my_value.left:
                stack.push(my_value.left)
