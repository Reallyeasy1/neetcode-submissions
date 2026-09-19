import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            heap = []
            for arr in points: 
                dist = (arr[0] ** 2 + arr[1] ** 2)
                heap.append([dist, arr[0], arr[1]])
            
            heapq.heapify(heap)
            op = []

            for i in range(k):
                arr = heapq.heappop(heap)
                x = arr[1]
                y = arr[2]
                op.append([x, y])

            return op