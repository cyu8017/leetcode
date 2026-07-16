# LeetCode 0824 - Goat Latin
# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        out = []
        for i, word in enumerate(sentence.split(), 1):
            if word[0] in vowels:
                goat = word + "ma"
            else:
                goat = word[1:] + word[0] + "ma"
            out.append(goat + "a" * i)
        return " ".join(out)
