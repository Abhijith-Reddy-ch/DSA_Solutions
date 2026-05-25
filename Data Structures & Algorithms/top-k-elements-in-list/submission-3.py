import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for item,freq in count.items():
            heapq.heappush(heap,(freq,item))

            if len(heap)>k:
                heapq.heappop(heap)
        
        return [item for freq,item in heap]