# LeetCode 1138 - Alphabet Board Path
# https://leetcode.com/problems/alphabet-board-path/

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        row, col = 0, 0
        ans: list[str] = []

        def move_to(r: int, c: int) -> None:
            nonlocal row, col
            while row < r:
                ans.append("D")
                row += 1
            while row > r:
                ans.append("U")
                row -= 1
            while col < c:
                ans.append("R")
                col += 1
            while col > c:
                ans.append("L")
                col -= 1

        for ch in target:
            r, c = divmod(ord(ch) - ord("a"), 5)
            if c < col and row == r:
                while col > c:
                    ans.append("L")
                    col -= 1
            else:
                move_to(r, c)
            ans.append("!")
        return "".join(ans)
