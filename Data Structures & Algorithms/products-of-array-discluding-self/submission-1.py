class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        start_mul = [1] * n
        end_mul = [1] * n
        prefix_mul = [1] * n
        

        for i in range(1, n):
            start_mul[i] = start_mul[i - 1] * nums[i-1]
        
        for i in range(n-2,-1,-1):
            end_mul[i] = end_mul[i+1] * nums[i+1]
        
        for i in range(n):
            prefix_mul[i] = start_mul[i] * end_mul[i]

        return prefix_mul