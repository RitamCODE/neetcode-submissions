from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k: # to maintain k largest
                heapq.heappop(heap)
    
        res = []
        for i in range(k):
            frequency, number = heapq.heappop(heap)
            res.append(number)
        return res