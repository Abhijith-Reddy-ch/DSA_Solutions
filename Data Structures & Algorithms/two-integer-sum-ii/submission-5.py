class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen ={}
        n=len(numbers)

        for i in range(n):
            diff = target-numbers[i]
            if diff in seen:
                return [seen[diff]+1,i+1]
            seen[numbers[i]] = i