# LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

from typing import List


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        tops = []
        for i in range(m):
            row = []
            for j in range(n):
                cur = {"v": board[i][j], "c": j}
                placed = False
                for t in range(len(row)):
                    if cur["v"] > row[t]["v"]:
                        row.insert(t, cur)
                        placed = True
                        break
                if not placed:
                    row.append(cur)
                if len(row) > 3:
                    row = row[:3]
            tops.append(row)
        ans = -(10**18)
        for i in range(m):
            for a in tops[i]:
                for j in range(i + 1, m):
                    for b in tops[j]:
                        if a["c"] == b["c"]:
                            continue
                        for k in range(j + 1, m):
                            for c in tops[k]:
                                if c["c"] == a["c"] or c["c"] == b["c"]:
                                    continue
                                s = a["v"] + b["v"] + c["v"]
                                if s > ans:
                                    ans = s
        return ans
