class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        j=0
        for ch in range(len(t)):

            if s[j]==t[ch]:
                j+=1
            if len(s)==j:
                break
        if len(s)!=j:
            return False
        return True
