# Reference: https://www.youtube.com/watch?v=k8F7nzySY60&t=712s&ab_channel=Pepcoding

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        sb = ""

        for i in range(numRows):
            index = i
            deltaSouth = 2*(numRows - 1 - i)
            deltaNorth = 2*i
            goingSouth = True

            while (index < len(s)):
                sb += s[index]

                if i == 0:
                    index += deltaSouth
                elif i == numRows - 1:
                    index += deltaNorth
                else:
                    if goingSouth:
                        index += deltaSouth
                    else:
                        index += deltaNorth
                    goingSouth = not goingSouth
        return sb