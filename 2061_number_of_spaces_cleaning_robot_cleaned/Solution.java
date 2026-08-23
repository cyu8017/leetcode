// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

import java.util.*;

class Solution {
    public int numberOfCleanRooms(int[][] room) {
        int m = room.length, n = room[0].length;
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        Set<Integer> vis = new HashSet<>();
        Set<Long> cleaned = new HashSet<>();
        cleaned.add(0L);
        int r = 0, c = 0, d = 0;
        while (vis.add(r * 10000 + c * 10 + d)) {
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr][nc] == 0) {
                r = nr; c = nc;
                cleaned.add((((long) r) << 32) ^ (c & 0xffffffffL));
            } else d = (d + 1) % 4;
        }
        return cleaned.size();
    }
}
