#
# Author: Vinhthuy Phan (04/2022)
# priority queue (max heap) of *hashable* data
#
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.priority = {}
        self.index = {}
    
    
    def put(self, data, priority):
        if data in self.priority:
            print('{} exists. Use method "adjust" to adjust priorities'.format(data))
            return
        self.heap.append(data)
        i = len(self.heap) - 1
        self.index[data] = i
        self.priority[data] = priority
        self.percolate_up(i)
    
    
    def get(self):
        if len(self.heap)==0:
            return
        item_priority = self.priority[self.heap[0]]
        item = self.heap[0]

        self.index[self.heap[-1]] = 0
        self.index.pop(self.heap[0])
        
        self.priority.pop(self.heap[0])
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        
        self.heap.pop(-1)
        
        self.percolate_down(0)
        
        return item, item_priority

    
    def adjust(self, data, priority):
        if data not in self.priority:
            print(data, 'is not in the queue.')
            return
        self.priority[data] = priority
        i = self.index[data]
        self.percolate_up(i)
        if i == self.index[data]:
            self.percolate_down(i)
    
    
    def percolate_up(self, i):
        while i>0:
            pid = (i-1)//2
            if self.priority[self.heap[pid]] < self.priority[self.heap[i]]:
                self.index[self.heap[pid]], self.index[self.heap[i]] = self.index[self.heap[i]], self.index[self.heap[pid]]
                self.heap[pid], self.heap[i] = self.heap[i], self.heap[pid]
                i = pid
            else:
                break


    def percolate_down(self, i):
        n = len(self.heap)
        while i*2+1 < n:
            lc = i*2 + 1
            rc = i*2 + 2
            if rc < n:
                if self.priority[self.heap[lc]] > self.priority[self.heap[rc]]:
                    idx = lc
                else:
                    idx = rc
            else:
                idx = lc
            if self.priority[self.heap[i]] > self.priority[self.heap[idx]]:
                return
            self.index[self.heap[i]], self.index[self.heap[idx]] = self.index[self.heap[idx]], self.index[self.heap[i]]
            self.heap[idx], self.heap[i] = self.heap[i], self.heap[idx]
            i = idx
        
    
    def __len__(self):
        return len(self.heap)
    
    
    def __contains__(self, data):
        return data in self.priority
    
        
    def __getitem__(self, data):
        return self.priority[data] if data in self.priority else None
    
    
    def debug(self):
        print('heap', self.heap, 'len =', len(self.heap))
        print('index', self.index, 'len=', len(self.index))
        print('priority', self.priority, 'len=', len(self.priority))
        print('priorities:', sorted(self.priority.values()))
        print()

