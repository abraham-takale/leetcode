class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9 +7
        even=(n+1)//2
        odd=n//2
        if n==1:
            return 5
        else:
             return(pow(5,even,MOD)*pow(4,odd,MOD))%MOD
