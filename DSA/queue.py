class Queue:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")
            
    def size(self):
        return len(self.items)
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue size:", q.size())  

print("Dequeue:", q.dequeue())  
print("Dequeue:", q.dequeue())  

print("Peek:", q.peek())  
print("Queue size:", q.size())  
