// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

using System.Collections.Generic;

public class Solution {
    public int MinFlips(int[][] mat) {
        int m = mat.Length, n = mat[0].Length;
        int start = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] != 0) start |= 1 << (r * n + c);
            }
        }
        var masks = new List<int>();
        int[][] deltas = { new[] { 0, 0 }, new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int mask = 0;
                foreach (var d in deltas) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) mask ^= 1 << (nr * n + nc);
                }
                masks.Add(mask);
            }
        }
        var queue = new Queue<(int state, int distance)>();
        var seen = new HashSet<int> { start };
        queue.Enqueue((start, 0));
        while (queue.Count > 0) {
            var (state, distance) = queue.Dequeue();
            if (state == 0) return distance;
            foreach (int mask in masks) {
                int nxt = state ^ mask;
                if (seen.Add(nxt)) queue.Enqueue((nxt, distance + 1));
            }
        }
        return -1;
    }
}
