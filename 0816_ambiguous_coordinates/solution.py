# LeetCode 0816 - Ambiguous Coordinates
# https://leetcode.com/problems/ambiguous-coordinates/

from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        digits = s[1:-1]

        def candidates(frag: str) -> list[str]:
            options: list[str] = []
            if not frag or (len(frag) > 1 and frag[0] == "0" and frag[-1] == "0"):
                return options
            if frag[0] == "0" and len(frag) > 1:
                return [f"0.{frag[1:]}"] if frag[-1] != "0" else []
            options.append(frag)
            if frag[-1] == "0":
                return options
            for i in range(1, len(frag)):
                options.append(f"{frag[:i]}.{frag[i:]}")
            return options

        answer: list[str] = []
        for i in range(1, len(digits)):
            for left in candidates(digits[:i]):
                for right in candidates(digits[i:]):
                    answer.append(f"({left}, {right})")
        return answer
