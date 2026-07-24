class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        result = []

        for word in words:

            if len(word) != len(pattern):
                continue

            map1 = {}
            map2 = {}

            valid = True

            for a, b in zip(word, pattern):

                if a in map1 and map1[a] != b:
                    valid = False
                    break

                if b in map2 and map2[b] != a:
                    valid = False
                    break

                map1[a] = b
                map2[b] = a

            if valid:
                result.append(word)

        return result
