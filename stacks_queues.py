# Examples of Stack:  A stack is Last In and First Out
import heapq
from collections import deque


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the top item of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack Examples")
print("Top item", stack.peek())
print("Size", stack.size())
print("Popped item", stack.pop())
print("Size after pop", stack.size())


# A Queue is First In First Out(FIFO)


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("dequeue from empty queue")

    def front(self):
        """Return the front item of the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("front from empty queue")

    def tail(self):
        """Return the back item of the queue without removing it."""
        if not self.is_empty():
            return self.queue[-1]
        raise IndexError("back from empty queue")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.queue)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)


print("Queue Examples")
print("Front item", queue.front())
print("Size", queue.size())
print("Dequeued item", queue.dequeue())
print("Size after dequeue", queue.size())
print("Front item in a Queue", queue.front())
print("Is queue empty?", queue.is_empty())
print("The last item in Queue", queue.tail)

# Priority Queue Example


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        """Add an item with a given priority."""
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        """Remove and return the item with the highest priority (lowest priority number)."""
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        raise IndexError("pop from empty priority queue")

    def peek(self):
        """Return the item with the highest priority without removing it."""
        if not self.is_empty():
            return self.heap[0][1]
        raise IndexError("peek from empty priority queue")

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap) == 0


pq = PriorityQueue()
pq.push("Task A", 3)  # Lower number = higher priority
pq.push("Task B", 1)
pq.push("Task C", 2)

print("Priority Queue Examples")
print("Highest priority item:", pq.peek())  # Highest priority item: Task B
print("Dequeued item:", pq.pop())  # Dequeued item: Task B
print("Dequeued item:", pq.pop())  # Dequeued item: Task C
print("The Peek_Front function", pq.peek_front())


"""Question 1:
    Baseball line up
    airplains waiting to taxi onto the runway.
    
  Question 2:
  boolean enq()
  boolean deq()
  boolean is_empty()
  boolean is_name()
  boolean is_parameters
  boolean is_return
  
  Question 3:
  Example function call(s)                  Results
  queue.is_empty()         []               true
  queue.enqueue(5)         []                 [5]
  queue.enqueue(3)         [5]               [5, 3]
  queue.enqueue(8)         [5, 3]            [5, 3, 8]
  queue.front())                                 5
  queue.tail()                                   8
  queue.is_empty()                             false
  -10 + (5 + (12 + 8) -2) + 1
  """


def eval(exp):
    result = 0
    n = 0  # Stores the last number
    sign = 1  # sign is 1 for a positive or -1 for a negative
    # Take a stack to store the sign
    stack = deque()
    stack.append(sign)

    #
