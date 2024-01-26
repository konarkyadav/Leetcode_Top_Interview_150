# Reference: https://www.youtube.com/watch?v=iu0082c4HDE&ab_channel=NeetCode
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        value = []

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/" :
                a = value.pop()
                b = value.pop()
                value.append(int(eval(str(b) + token + str(a))))
            else:
                value.append(token)
        
        return int(value[0])