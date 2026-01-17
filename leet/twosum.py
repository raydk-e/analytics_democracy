class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, item in enumerate(nums):
            diff = target - item
            
            if diff in seen:
                return [seen[diff],i]
            seen[item] = i
s = Solution()
print(s.twoSum([2, 3,4, 11, 6], 9))