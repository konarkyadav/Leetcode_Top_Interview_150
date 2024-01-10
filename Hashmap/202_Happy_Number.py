# class Solution:
#     def isHappy(self, n: int) -> bool:
#         dp = {}
#         def dfs(num):
#             if num in dp:
#                 return dp[num]
#             else:
#                 summation = 0
#                 num_temp = num
#                 while num_temp > 0:
#                     mod = num_temp%10
#                     summation += mod**2
#                     num_temp = num_temp//10
#                 dp[num] = summation
#                 return dfs(summation)
#         return dfs(n) == 1

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1