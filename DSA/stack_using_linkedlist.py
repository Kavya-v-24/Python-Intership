class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Stack:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None
    
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def pop(self):
        if self.is_empty():
            return None
        popped=self.head.next
        return popped
    
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
        
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print("popped:",stack.pop())
print("peek:",stack.peek())
stack.display()
