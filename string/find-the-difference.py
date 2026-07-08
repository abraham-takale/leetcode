class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp=list(t)
        for ch in s:
            temp.remove(ch)
        return "".join(temp)
