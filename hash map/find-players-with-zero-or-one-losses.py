class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic={}
        ans1=[]
        ans2=[]
        for winner,loser in matches:
            if winner not in dic:
                dic[winner]=0
            if loser not in dic:
                dic[loser]=1
            else:
                dic[loser] +=1
        for i in dic:
            if dic[i]==0:
                ans1.append(i)
            elif dic[i]==1:
                ans2.append(i)
        ans1.sort()
        ans2.sort()
        return([ans1,ans2])
