class Solution:
    def longestPalindrome(self, s: str) -> int:
        num = 0
        has_odd = False
        freq = []
        for ch in s:
            if ch not in freq:
                freq.append(ch)
                count = s.count(ch)

                if count % 2 == 0:
                    num += count
                else:
                    num += count - 1
                    has_odd = True

        if has_odd:
            return num + 1

        return num
