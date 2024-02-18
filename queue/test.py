'''
Queue class testing.
'''


from queue import LinearQueue


# Queue instance
queue = LinearQueue(5)
print(queue)

# Enqueues
queue.enqueue('A')
print(queue)
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

queue.enqueue('F') # Queue Overflow (need of circular queue)

print('Value Dequeued:', queue.dequeue())
print('Value Dequeued:', queue.dequeue())
print('Value Dequeued:', queue.dequeue())
print(queue)
print('Value Dequeued:', queue.dequeue()) # Queue Underflow (2nd scenario)

queue_2 = LinearQueue(5)
print(queue_2)
print('Value Dequeued:', queue_2.dequeue())# Queue Underflow (1st scenario)




