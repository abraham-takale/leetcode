class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ch in  range(len(s)):
            if s.count(s[ch])==1:
                return ch
        
        return -1
