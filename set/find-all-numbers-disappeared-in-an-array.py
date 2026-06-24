 def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        se=set(nums)
        for i in range(1,len(nums)+1):
            if i not in se:
                result.append(i)
        return result 
