# LeetCode 0726 - Number of Atoms
# https://leetcode.com/problems/number-of-atoms/

from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack: list[Counter[str]] = [Counter()]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == "(":
                stack.append(Counter())
                i += 1
            elif formula[i] == ")":
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i] or "1")
                top = stack.pop()
                for atom, count in top.items():
                    stack[-1][atom] += count * mult
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or "1")
                stack[-1][atom] += count

        counts = stack.pop()
        parts: list[str] = []
        for atom in sorted(counts):
            parts.append(atom)
            if counts[atom] > 1:
                parts.append(str(counts[atom]))
        return "".join(parts)
