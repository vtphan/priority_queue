This implementation of priority queues lets users adjust priorities of stored data.  While Python's standard libraries include an implementation of priority queues, priorities of data are not adjustable after they are stored.

To use this priority queue, data must be hashable, e.g. numbers, strings, tuples.  For unhashable data, this can be done by storing their hashable id's.

Usage:
```
from priority_queue import PriorityQueue
import random

Q = PriorityQueue()
for data in 'abcdefgh':
    priority = random.randint(1,100)
    Q[data] = priority  ### or Q.put(data, priority)
    print('insert', data, 'with priority', priority)

print('\nadjust priority of "a" to 120\n')
Q['a'] = 120    ### or Q.adjust('a', 120)

while len(Q) > 0:
    data, priority = Q.get()
    print('removed', data, 'with priority', priority)
```