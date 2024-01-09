class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = Counter(s)
        word2 = Counter(t)
        return word1==word2