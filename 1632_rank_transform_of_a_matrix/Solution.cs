// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[][] MatrixRankTransform(int[][] matrix) {
        int m = matrix.Length, n = matrix[0].Length;
        var groups = new SortedDictionary<int, List<(int i, int j)>>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!groups.ContainsKey(matrix[i][j])) groups[matrix[i][j]] = new List<(int, int)>();
                groups[matrix[i][j]].Add((i, j));
            }
        }
        var rank = new int[m + n];
        var ans = new int[m][];
        for (int i = 0; i < m; i++) ans[i] = new int[n];
        foreach (var cells in groups.Values) {
            var parent = new Dictionary<int, int>();
            int Find(int x) {
                if (!parent.ContainsKey(x)) parent[x] = x;
                if (parent[x] != x) parent[x] = Find(parent[x]);
                return parent[x];
            }
            foreach (var (i, j) in cells) {
                int a = Find(i), b = Find(m + j);
                parent[a] = b;
            }
            var best = new Dictionary<int, int>();
            foreach (var (i, j) in cells) {
                int root = Find(i);
                best[root] = Math.Max(best.GetValueOrDefault(root), Math.Max(rank[i], rank[m + j]));
            }
            foreach (var (i, j) in cells) ans[i][j] = best[Find(i)] + 1;
            foreach (var (i, j) in cells) {
                rank[i] = Math.Max(rank[i], ans[i][j]);
                rank[m + j] = Math.Max(rank[m + j], ans[i][j]);
            }
        }
        return ans;
    }
}
