// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

import java.util.*;

class Solution {
    public int numberOfPaths(int n, int[][] corridors) {
        Set<Integer>[] g = new HashSet[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new HashSet<>();
        for (int[] e : corridors) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int ans = 0;
        for (int[] e : corridors) {
            int a = e[0], b = e[1];
            for (int c : g[a]) if (g[b].contains(c)) ans++;
        }
        return ans / 3;
    }
}
