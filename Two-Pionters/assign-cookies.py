class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        right=0
        left=0
        g.sort()
        s.sort()
        while left<len(g) and right<len(s):
            if g[left]<=s[right]:
                left+=1 
            right+=1   
        return left
