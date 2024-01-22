# https://www.youtube.com/watch?v=44H3cEC2fFM&ab_channel=NeetCode
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        prev = 0
        count = 0

        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                count += 1
            else:
                prev = i
        return count