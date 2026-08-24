# LeetCode 2047 - Number of Valid Words in a Sentence
# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/


class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(w: str) -> bool:
            if not w:
                return False
            hyphen = 0
            for i, c in enumerate(w):
                if "0" <= c <= "9":
                    return False
                if c == "-":
                    hyphen += 1
                    if hyphen > 1 or i == 0 or i == len(w) - 1:
                        return False
                    if not ("a" <= w[i - 1] <= "z" and "a" <= w[i + 1] <= "z"):
                        return False
                elif c in "!.,":
                    if i != len(w) - 1:
                        return False
                elif not ("a" <= c <= "z"):
                    return False
            return True

        return sum(1 for tok in sentence.split(" ") if valid(tok))
