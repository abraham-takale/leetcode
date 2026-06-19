class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        che=[]
        for i in nums1:
            if i in nums2 and i not in che:
                che.append(i)
        return che
