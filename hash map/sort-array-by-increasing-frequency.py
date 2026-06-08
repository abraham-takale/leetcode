class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        arr = []
        for num in sorted(freq, key=lambda x: (freq[x], -x)):
            arr.extend([num] * freq[num])
        return arr
