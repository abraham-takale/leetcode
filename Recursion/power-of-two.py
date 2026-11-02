class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n==0:
            return False
        while n>=2:
            if n%2!=0:
                return False
                break
            x=n
            n//=2
            if x%2==0 and n==1:
                return True
        return False
