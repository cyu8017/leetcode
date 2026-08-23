// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

import java.util.*;

class Solution {
    public int shortestPathAllKeys(String[] grid) {
        int m = grid.length, n = grid[0].length();
        int allKeys = 0, sr = 0, sc = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char ch = grid[i].charAt(j);
                if (ch == '@') { sr = i; sc = j; }
                else if (ch >= 'a' && ch <= 'f') allKeys |= 1 << (ch - 'a');
            }
        }
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {sr, sc, 0, 0});
        Set<Long> seen = new HashSet<>();
        seen.add(encode(sr, sc, 0));
        int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0], c = cur[1], mask = cur[2], dist = cur[3];
            if (mask == allKeys) return dist;
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr].charAt(nc) == '#') continue;
                char cell = grid[nr].charAt(nc);
                int nmask = mask;
                if (cell >= 'a' && cell <= 'f') nmask |= 1 << (cell - 'a');
                if (cell >= 'A' && cell <= 'F' && (mask & (1 << (cell - 'A'))) == 0) continue;
                if (seen.add(encode(nr, nc, nmask))) queue.offer(new int[] {nr, nc, nmask, dist + 1});
            }
        }
        return -1;
    }

    private long encode(int r, int c, int mask) {
        return ((long) r << 20) | ((long) c << 10) | mask;
    }
}
