// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

class Solution {
    public int[][] colorGrid(int n, int m, int[][] sources) {
        int[][] ans = new int[n][m];
        List<int[]> q = new ArrayList<>();
        for (int[] s : sources) q.add(s);
        int[] dirs = { -1, 0, 1, 0, -1 };
        for (int[] s : q) ans[s[0]][s[1]] = s[2];
        while (!q.isEmpty()) {
            TreeMap<Long, Integer> vis = new TreeMap<>();
            for (int[] curr : q) {
                int r = curr[0], c = curr[1], color = curr[2];
                for (int i = 0; i < 4; i++) {
                    int x = r + dirs[i], y = c + dirs[i + 1];
                    if (x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0) {
                        long key = ((long) x << 32) | (y & 0xffffffffL);
                        if (!vis.containsKey(key) || color > vis.get(key)) vis.put(key, color);
                    }
                }
            }
            q.clear();
            for (var kv : vis.entrySet()) {
                long key = kv.getKey();
                int x = (int) (key >> 32);
                int y = (int) key;
                int color = kv.getValue();
                ans[x][y] = color;
                q.add(new int[] { x, y, color });
            }
        }
        return ans;
    }
}
