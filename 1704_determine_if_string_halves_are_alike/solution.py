class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        mid = len(s) // 2
        return sum(ch in vowels for ch in s[:mid]) == sum(ch in vowels for ch in s[mid:])
