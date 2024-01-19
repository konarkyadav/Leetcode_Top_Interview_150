# Reference: https://www.youtube.com/watch?v=aYqYMIqZx5s&ab_channel=NeetCode
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0, 0
        res = float("inf")

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(right - left + 1, res)
                total -= nums[left]
                left += 1

        if res == float("inf"):
            return 0
        else:
            return res