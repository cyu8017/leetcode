# LeetCode 3481 - Apply Substitutions
# https://leetcode.com/problems/apply-substitutions/

from typing import List


class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mp = {r[0]: r[1] for r in replacements}

        def resolve(s: str) -> str:
            out = []
            i = 0
            while i < len(s):
                if s[i] == "%":
                    j = i + 1
                    while j < len(s) and s[j] != "%":
                        j += 1
                    key = s[i + 1 : j]
                    out.append(resolve(mp[key]))
                    i = j + 1
                else:
                    out.append(s[i])
                    i += 1
            return "".join(out)

        return resolve(text)
