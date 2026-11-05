class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        path=[]
        def backtrack():
            if len(path)==len(nums):
                ans.append(path.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack()
                    path.pop()
        backtrack()
        return ans
