class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

task_queue = Queue() 
task_queue.enqueue("Excavation")
task_queue.enqueue("Foundation")
print(task_queue.dequeue())
print(task_queue.peek()) 
