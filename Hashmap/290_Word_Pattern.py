class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = []
        map2 = []
        for i in pattern:
            map1.append(pattern.index(i))
        words = s.split()
        for word in words:
            map2.append(words.index(word))
        return map1==map2