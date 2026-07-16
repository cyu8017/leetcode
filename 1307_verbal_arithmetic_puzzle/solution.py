# LeetCode 1307 - Verbal Arithmetic Puzzle

from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if max(map(len, words)) > len(result):
            return False
        if len(set("".join(words) + result)) > 10:
            return False
        leading = {word[0] for word in words + [result] if len(word) > 1}
        value, used = {}, [False] * 10
        width = len(result)

        def solve(column: int, row: int, total: int) -> bool:
            if column == width:
                return total == 0
            if row < len(words):
                if column >= len(words[row]):
                    return solve(column, row + 1, total)
                ch = words[row][-1 - column]
                if ch in value:
                    return solve(column, row + 1, total + value[ch])
                for digit in range(10):
                    if not used[digit] and (digit or ch not in leading):
                        value[ch] = digit; used[digit] = True
                        if solve(column, row + 1, total + digit):
                            return True
                        used[digit] = False; del value[ch]
                return False
            ch = result[-1 - column]
            digit = total % 10
            carry = total // 10
            if ch in value:
                return value[ch] == digit and solve(column + 1, 0, carry)
            if used[digit] or (digit == 0 and ch in leading):
                return False
            value[ch] = digit; used[digit] = True
            ok = solve(column + 1, 0, carry)
            used[digit] = False; del value[ch]
            return ok

        return solve(0, 0, 0)
