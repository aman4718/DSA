class Queue:
    def __init__(self):
        self.queue = []

    # adds an item to the end of the list using 
    def enqueue(self, item):
        self.queue.append(item)

    #  removes and returns the first item from the list using
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty. Cannot dequeue from an empty queue.")

    # check is empty 
    def isEmpty(self):
        return len(self.queue) == 0


my_queue = Queue()
my_queue.enqueue(55)
my_queue.enqueue(60)
my_queue.enqueue(70)

# calling
print(my_queue.dequeue())  #output 55
print(my_queue.dequeue())  #output 60
print(my_queue.isEmpty())  #output False
print(my_queue.dequeue())  #output 70
print(my_queue.isEmpty())  #output True

