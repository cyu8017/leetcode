# LeetCode 2056 - Number of Valid Move Combinations On Chessboard
# https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

from typing import List


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        dirs = {
            "rook": [(1, 0), (-1, 0), (0, 1), (0, -1)],
            "bishop": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            "queen": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)],
        }
        n = len(pieces)
        all_moves = []
        for i in range(n):
            ms = [{"dr": 0, "dc": 0, "steps": 0}]
            r, c = positions[i]
            for dr, dc in dirs[pieces[i]]:
                nr, nc, step = r + dr, c + dc, 1
                while 1 <= nr <= 8 and 1 <= nc <= 8:
                    ms.append({"dr": dr, "dc": dc, "steps": step})
                    nr += dr
                    nc += dc
                    step += 1
            all_moves.append(ms)
        chosen = [None] * n
        ans = 0

        def ok_combo(end: int) -> bool:
            max_t = max(chosen[i]["steps"] for i in range(end + 1))
            for t in range(1, max_t + 1):
                seen = set()
                for i in range(end + 1):
                    m = chosen[i]
                    if m["steps"] == 0:
                        pr, pc = positions[i]
                    else:
                        use = min(t, m["steps"])
                        pr = positions[i][0] + m["dr"] * use
                        pc = positions[i][1] + m["dc"] * use
                    key = (pr << 32) ^ (pc & 0xFFFFFFFF)
                    if key in seen:
                        return False
                    seen.add(key)
            return True

        def dfs(i: int) -> None:
            nonlocal ans
            if i == len(pieces):
                ans += 1
                return
            for m in all_moves[i]:
                chosen[i] = m
                if ok_combo(i):
                    dfs(i + 1)

        dfs(0)
        return ans
