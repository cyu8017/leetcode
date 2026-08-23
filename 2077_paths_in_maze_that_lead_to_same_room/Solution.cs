// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

using System.Collections.Generic;

public class Solution {
    public int NumberOfPaths(int n, int[][] corridors) {
        var g = new HashSet<int>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new HashSet<int>();
        foreach (var e in corridors) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int ans = 0;
        foreach (var e in corridors) {
            int a = e[0], b = e[1];
            foreach (int c in g[a]) if (g[b].Contains(c)) ans++;
        }
        return ans / 3;
    }
}
