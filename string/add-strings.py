class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1=len(num1)-1
        n2=len(num2)-1
        carry=0
        result=""
        while n1 >= 0 or n2 >= 0:
            a=ord(num1[n1])-ord("0") if n1>=0 else 0
            b=ord(num2[n2])-ord("0") if n2>=0 else 0
            total=a+b+carry
            result=chr(total%10 + ord("0")) + result
            carry=total//10
            n1-=1
            n2-=1
        return result
