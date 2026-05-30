from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=Counter(s)
        b=Counter(t)
        if len(s)!=len(t):
            return False
        for letter in a:
            if a[letter]!=b[letter]:
                return False
        return True
