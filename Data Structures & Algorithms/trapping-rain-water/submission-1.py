class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0]*n
        suffix = [0]*n
        maxi = 0

        for i in range(n):
            if height[i]>maxi:
                prefix[i] = height[i]
                maxi = height[i]
            else:
                prefix[i] = maxi

        maxi = 0
        for i in range(n-1,-1,-1):
            if height[i]>maxi:
                suffix[i] = height[i]
                maxi = height[i]
            else:
                suffix[i] = maxi
        ans = 0
        for i in range(n):
            ans += min(prefix[i],suffix[i])-height[i]
        
        return ans