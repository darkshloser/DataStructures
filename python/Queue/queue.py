from collections import deque


class Queue:

    def __init__(self):
        self._queue = deque()

    def enqueue(self, item):
        """Add item to the end of the queue"""
        self._queue.append(item)

    def dequeue(self):
        """Remove item from the queue (front of the queue)"""
        if self.is_empty():
            raise IndexError("Queue is empty and 'dequeue' operation not allowed")
        return self._queue.popleft()

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self._queue) == 0
    
    def size(self):
        """Size of the queue"""
        return len(self._queue)
    
    def pop_view(self):
        """View the front element of the queue"""
        if self.is_empty():
            return None
        return self._queue[0]

    def __str__(self):
        return f"Queue is: {list(self._queue)}"


