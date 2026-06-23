class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        ad=[]
        nu1c=0
        nu2c=0
        for i in nums1:
            if i in nums2 and i not in result:
                nu1c=nums1.count(i)
                nu2c=nums2.count(i)
                if nu1c<=nu2c:
                    ad=[i]*nu1c
                    result.extend(ad)
                else:
                    ad=[i]*nu2c
                    result.extend(ad)
        return result
