This implementation of priority queues let users adjust priorities of stored data.  While Python's standard libraries include an implementation of priority queues, priorities of data are not adjustable after they are stored.

To use this priority queue, data must be hashable, e.g. numbers, strings, tuples.  For unhashable data, this can be done by storing their hashable id's.

Usage:
```
import random
q = PriorityQueue()
for c in 'abcdefgh':
    p = random.randint(1,100)
    print('insert', c, 'with priority', p)
    q.put(c, p)

print('\nadjust priority of "a" to 120\n')
q.adjust_priority('a', 120)

while len(q.heap) > 0:
    c, p = q.remove_most_prioritized()
    print('removed', c, 'with priority', p)
```