import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}

        for x in nums:
            freq[x] = freq.get(x,0)+1

        top_k = heapq.nlargest(k, freq, key=freq.get)

        return top_k