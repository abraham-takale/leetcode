class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n ==1:
            return True
        while n>=4:
            x=n
            n//=4
            if x%4==0 and n==1:
                return True
            elif x%4!=0:
                return False
        return False
