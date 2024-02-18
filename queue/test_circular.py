'''
Queue class testing.
'''


from queue_circular import CircularQueue


# Queue instance
queue = CircularQueue(5)
print(queue)

#1st underflow
print('Value Dequeued:', queue.dequeue())

# Enqueues
queue.enqueue('A')
queue.enqueue('B')
print(queue)
queue.enqueue('C')
queue.enqueue('D')
queue.enqueue('E')
print(queue)
queue.enqueue('F') # Queue Overflow

# Dequeues
print('Value Dequeued:', queue.dequeue())
print(queue)
print('Value Dequeued:', queue.dequeue())
print(queue)

queue.enqueue('F') # Avoids overflow succesfully
print(queue)

queue.enqueue('G') # Avoids overflow succesfully
print(queue)
queue.enqueue('H') # Overflow 2nd scenario (not in book's pseudocode)
print(queue)

print('Value Dequeued:', queue.dequeue())
print('Value Dequeued:', queue.dequeue())
print('Value Dequeued:', queue.dequeue())
print(queue)
print('Value Dequeued:', queue.dequeue()) 
print(queue)
print('Value Dequeued:', queue.dequeue())
print(queue)
