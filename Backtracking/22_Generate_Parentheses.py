# Reference: https://www.youtube.com/watch?v=s9fokUqJ76A&ab_channel=NeetCode

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(open, close, output):
            if len(output) == n*2:
                result.append(output)
                return result

            if open < n:
                dfs(open+1, close, output + "(")
            if close < open:
                dfs(open, close + 1, output + ")")

        dfs(0,0,"")
        return result

