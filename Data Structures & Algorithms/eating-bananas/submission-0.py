class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        if len(piles) == h:
            return k
        
        low = 1
        high = k
        result = k

        while low<=high:
            mid = (low+high) // 2

            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile/mid)
            
            if total_hours <= h:
                result = mid
                high  = mid -1
            else:
                low = mid+1
        return result
