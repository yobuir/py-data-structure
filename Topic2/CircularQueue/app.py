class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            return "Circular Queue is full"
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
    
    def dequeue(self):
        if self.is_empty():
            return "Circular Queue is empty"
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def peek(self):
        if self.is_empty():
            return "Circular Queue is empty"
        return self.queue[self.front]

# Example Usage:
circular_task_queue = CircularQueue(3)
circular_task_queue.enqueue("Weekly Safety Check")
circular_task_queue.enqueue("Progress Meeting")
print(circular_task_queue.dequeue())
circular_task_queue.enqueue("Equipment Maintenance")
print(circular_task_queue.peek())   
circular_task_queue.enqueue("New Task")  
