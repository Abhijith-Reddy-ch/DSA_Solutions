class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        seen = {}

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = n-1

            while l<r:
                three_sum = nums[i]+nums[l]+nums[r]
                if three_sum == 0:
                        ans.append([nums[i],nums[l],nums[r]])
                        l+=1
                        r-=1

                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        while l<r and nums[r] == nums[r+1]:
                            r -= 1
                elif three_sum <0:
                    l += 1
                else:
                    r-=1
        return ans

