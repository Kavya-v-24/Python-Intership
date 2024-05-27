class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class QueueLinkedList:
  def __init__(self):
    self.front=None
    self.rear=None

  def is_empty(self):
    return self.front is None

  def enqueue(self,item):
    new_node=Node(item)
    if self.is_empty():
      self.front=new_node
      self.rear=new_node
    else:
      self.rear.next=new_node
      self.rear=new_node

  def dequeue(self):
    if not self.is_empty():
      dequeued_item=self.front.data
      self.front=self.front.next
      if self.front is None:
        self.rear=None
      return dequeued_item
    else:
      raise IndexError("dequeue from an empty queue")

  def peek(self):
    if not self.is_empty():
      return self.front.data
    else:
      raise IndexError("Peek from an empty queue")

  def size(self):
    count=1
    current=self.front
    while current:
      count+=1
      current=current.next
    return count

queue=QueueLinkedList()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
queue.enqueue(80)
queue.enqueue(90)

print("Front of the queue: ",queue.peek())

print("Dequeue: ",queue.dequeue())

print("Size: ",queue.size())