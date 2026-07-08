class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        vowels=["A","E","I","O","U","a","e","i","o","u"]
        n=len(l)-1
        m=0
        while m<n:
            if l[n] not in vowels and l[m] not in vowels:
                n-=1
                m+=1
            elif l[n] not in vowels:
                n-=1
            elif l[m] not in vowels :
                m+=1
            else :
                l[m],l[n]=l[n],l[m]
                m+=1
                n-=1
        return "".join(l)
