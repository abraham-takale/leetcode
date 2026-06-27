class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=0
        n=len(mat)
        for i in range(n):
            sum1+=mat[i][i]
            sum1+=mat[i][n-1-i]
        if n%2==1:
            sum1-=mat[n//2][n//2]
        return sum1
