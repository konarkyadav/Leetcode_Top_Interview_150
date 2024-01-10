class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def convert(a, b):
            if a == b:
                return str(a)
            else:
                return f"{a}->{b}"
        result = []
        i=0

        while i < len(nums):
            start = nums[i]
            while i < len(nums)-1 and nums[i+1] - nums[i] == 1:
                i+=1
            end = nums[i]
            result.append(convert(start, end))
            i+=1
        return result