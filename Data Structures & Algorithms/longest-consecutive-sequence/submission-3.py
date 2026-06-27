class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        hash_set = set(nums)
        longest = 0

        for num in nums:
            if num-1 not  in hash_set:
                count = 1
                curr = num

                while curr+1 in hash_set:
                    curr = curr+1
                    count += 1
                longest = max(longest,count)
        return longest