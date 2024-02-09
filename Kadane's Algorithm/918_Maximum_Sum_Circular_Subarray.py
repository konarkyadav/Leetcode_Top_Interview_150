class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = nums[0]
        globalMin = nums[0]
        currMax = 0
        currMin = 0
        total = 0

        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
            total += num
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
        
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax

# https://www.youtube.com/watch?v=fxT9KjakYPM&ab_channel=NeetCodeIO