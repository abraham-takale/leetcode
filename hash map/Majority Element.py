def majorityElement(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for key in dic:
            if dic[key] > n/2:
                return key
