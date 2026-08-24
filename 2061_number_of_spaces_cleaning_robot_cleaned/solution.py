# LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
# https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

from typing import List


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = set()
        cleaned = {0}
        r = c = d = 0
        while True:
            state = r * 10000 + c * 10 + d
            if state in vis:
                break
            vis.add(state)
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            if 0 <= nr < m and 0 <= nc < n and room[nr][nc] == 0:
                r, c = nr, nc
                cleaned.add((r << 32) ^ (c & 0xFFFFFFFF))
            else:
                d = (d + 1) % 4
        return len(cleaned)
