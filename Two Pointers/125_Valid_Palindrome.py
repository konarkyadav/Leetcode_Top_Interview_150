# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = ''.join(char.lower() for char in s if char.isalnum())
#         return s == s[::-1]

class Solution:

    def check_palindrom(self, left, right, new_str):
        if (left >= right):
            return True
        if new_str[left] == new_str[right]:
            return self.check_palindrom(left+1, right-1, new_str)

    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum():
                i = i.lower()
                new_str += i
        
        return self.check_palindrom(0, len(new_str)-1, new_str)