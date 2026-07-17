# LeetCode 1807 - Evaluate the Bracket Pairs of a String
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = {key: value for key, value in knowledge}
        result: list[str] = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                j = s.find(")", i + 1)
                key = s[i + 1 : j]
                result.append(lookup.get(key, "?"))
                i = j + 1
            else:
                result.append(s[i])
                i += 1
        return "".join(result)
