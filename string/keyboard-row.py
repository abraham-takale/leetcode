class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result=[]
        r1="qwertyuiop"
        r2="asdfghjkl"
        r3="zxcvbnm"
        for i in range(len(words)):
            if all(ch in r1 for ch in words[i].lower()):
                result.append(words[i])
            if all(ch in r2 for ch in words[i].lower()):
                result.append(words[i])
            if all(ch in r3 for ch in words[i].lower()):
                result.append(words[i])
        return result
