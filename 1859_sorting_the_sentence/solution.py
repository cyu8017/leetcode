# LeetCode 1859 - Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        tokens = s.split()
        ordered = [""] * len(tokens)

        for token in tokens:
            position = int(token[-1]) - 1
            ordered[position] = token[:-1]

        return " ".join(ordered)
