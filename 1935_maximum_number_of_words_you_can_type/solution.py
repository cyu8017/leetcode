class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(1 for w in text.split() if not broken.intersection(w))
