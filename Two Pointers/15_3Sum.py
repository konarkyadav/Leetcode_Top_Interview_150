# Reference: https://www.youtube.com/watch?v=E7Ie6OlQgN4&ab_channel=PrakashShukla
# https://www.youtube.com/watch?v=jzZsG8n2R9A&ab_channel=NeetCode
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                else:
                    result.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1
        
        return result