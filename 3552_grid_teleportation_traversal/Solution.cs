// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

using System.Collections.Generic;

public class Solution {
    public int MinMoves(string[] matrix) {
        int m = matrix.Length, n = matrix[0].Length;
        var g = new Dictionary<char, List<(int, int)>>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (char.IsLetter(matrix[i][j])) {
                    if (!g.ContainsKey(matrix[i][j])) g[matrix[i][j]] = new List<(int, int)>();
                    g[matrix[i][j]].Add((i, j));
                }
        int[] dirs = { -1, 0, 1, 0, -1 };
        const int INF = 1 << 30;
        int[][] dist = new int[m][];
        for (int i = 0; i < m; i++) {
            dist[i] = new int[n];
            for (int j = 0; j < n; j++) dist[i][j] = INF;
        }
        dist[0][0] = 0;
        var q = new LinkedList<(int, int)>();
        q.AddLast((0, 0));
        while (q.Count > 0) {
            var (i, j) = q.First.Value;
            q.RemoveFirst();
            int d = dist[i][j];
            if (i == m - 1 && j == n - 1) return d;
            char c = matrix[i][j];
            if (g.ContainsKey(c)) {
                foreach (var (x, y) in g[c]) {
                    if (d < dist[x][y]) {
                        dist[x][y] = d;
                        q.AddFirst((x, y));
                    }
                }
                g.Remove(c);
            }
            for (int idx = 0; idx < 4; idx++) {
                int x = i + dirs[idx], y = j + dirs[idx + 1];
                if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] != '#' && d + 1 < dist[x][y]) {
                    dist[x][y] = d + 1;
                    q.AddLast((x, y));
                }
            }
        }
        return -1;
    }
}
