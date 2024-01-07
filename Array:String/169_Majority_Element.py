# Reference: https://www.youtube.com/watch?v=7pnhv842keE&ab_channel=NeetCode
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

        # set_nums = set(nums)

        # for val in set_nums:
        #     if nums.count(val) > len(nums)//2:
        #         return val