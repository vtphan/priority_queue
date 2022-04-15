This module provides class PriorityQueue, which is a priority queue (max heap) for hashable (immutable) data types.

Unlike, Python's built-in heapq or PriorityQueue, this implementation allows adjustments of priorities of stored data.

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