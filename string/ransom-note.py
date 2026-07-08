class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch not in magazine or ransomNote.count(ch)>magazine.count(ch):
                return False
        return True
