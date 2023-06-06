def enqueues(queue, value):
    queue.append(value)


def dequeues(queue):
    return queue.pop()


my_queue = []
enqueues(my_queue, 'a')
enqueues(my_queue, 'b')
enqueues(my_queue, 'c')

print(my_queue)
