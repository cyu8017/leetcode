// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

using System.Collections.Generic;

public class Solution {
    public int[][] HighestPeak(int[][] isWater) {
        int m = isWater.Length;
        int n = isWater[0].Length;
        var dist = new int[m][];
        for (int i = 0; i < m; i++) {
            dist[i] = new int[n];
            for (int j = 0; j < n; j++) {
                dist[i][j] = -1;
            }
        }
        var queue = new Queue<(int, int)>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (isWater[i][j] == 1) {
                    dist[i][j] = 0;
                    queue.Enqueue((i, j));
                }
            }
        }
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        while (queue.Count > 0) {
            var (i, j) = queue.Dequeue();
            foreach (var d in dirs) {
                int x = i + d[0];
                int y = j + d[1];
                if (x >= 0 && x < m && y >= 0 && y < n && dist[x][y] == -1) {
                    dist[x][y] = dist[i][j] + 1;
                    queue.Enqueue((x, y));
                }
            }
        }
        return dist;
    }
}
