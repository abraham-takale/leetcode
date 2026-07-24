class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1={}
        map2={}
        words=s.split()
        if len(words) != len(pattern):
            return False
        for a,b in zip(words,pattern):
            if a in map1 and map1[a]!=b:
                return False
            if b in map2 and map2[b]!=a:
                return False
            map1[a]=b
            map2[b]=a
        
        return True
