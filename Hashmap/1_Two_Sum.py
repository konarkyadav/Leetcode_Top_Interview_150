# Reference: https://www.youtube.com/watch?v=KLlXCFG5TnA&t=15s&ab_channel=NeetCode

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
        
#         return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevVal = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevVal:
                return [prevVal[difference], i]
            prevVal[n] = i
        return []