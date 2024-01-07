# Reference: https://www.youtube.com/watch?v=ycAq8iqh0TI&ab_channel=NeetCodeIO

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        occurance = 1
        index = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            else:
                occurance = 1
            
            if occurance < 3:
                nums[index] = nums[i]
                index += 1
        
        return index