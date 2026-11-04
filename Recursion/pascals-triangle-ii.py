class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        n=rowIndex
        ans=[1]
        for i in range(n):
            prev=[1]
            for j in range(len(ans)-1):
                prev.append(ans[j]+ans[j+1])
            prev.append(1)
            ans=prev
        return ans
