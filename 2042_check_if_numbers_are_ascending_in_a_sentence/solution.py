# LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for tok in s.split(" "):
            if not tok:
                continue
            if "0" <= tok[0] <= "9":
                v = int(tok)
                if v <= prev:
                    return False
                prev = v
        return True
