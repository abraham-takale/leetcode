class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse=0
        origional=x
        while x:
            reverse=reverse *10+x%10
            x//=10
        return origional==reverse
