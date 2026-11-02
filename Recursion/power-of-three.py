    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        while n>=3:
            if n%3!=0:
                return False
            x=n
            n//=3
            if x%3==0 and n==1:
                return True
        return False
