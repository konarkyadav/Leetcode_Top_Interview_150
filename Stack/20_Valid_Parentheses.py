# Reference: https://www.youtube.com/watch?v=WTzjTskDFMg&ab_channel=NeetCode
class Solution:
    def isValid(self, s: str) -> bool:
        symbols = []
        for c in s:
            if c in ["(", "[", "{"]:
                symbols.append(c)
            elif(c == ")" and len(symbols) != 0 and symbols[-1] == "("):
                symbols.pop()
            elif(c == "]" and len(symbols) != 0 and symbols[-1] == "["):
                symbols.pop()
            elif(c == "}" and len(symbols) != 0 and symbols[-1] == "{"):
                symbols.pop()
            else:
                return False
        return symbols == []
            