// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxPartitionFactor(int[][] points) {
        int n = points.Length;
        if (n == 2) return 0;
        int Dist(int i, int j) {
            return Math.Abs(points[i][0] - points[j][0]) + Math.Abs(points[i][1] - points[j][1]);
        }
        bool Ok(int d) {
            var g = new List<int>[n];
            for (int i = 0; i < n; i++) g[i] = new List<int>();
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (Dist(i, j) < d) {
                        g[i].Add(j);
                        g[j].Add(i);
                    }
                }
            }
            int[] color = new int[n];
            Array.Fill(color, -1);
            for (int i = 0; i < n; i++) {
                if (color[i] != -1) continue;
                var q = new Queue<int>();
                q.Enqueue(i);
                color[i] = 0;
                while (q.Count > 0) {
                    int u = q.Dequeue();
                    foreach (int v in g[u]) {
                        if (color[v] == -1) {
                            color[v] = color[u] ^ 1;
                            q.Enqueue(v);
                        } else if (color[v] == color[u]) return false;
                    }
                }
            }
            return true;
        }
        int lo = 0, hi = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                hi = Math.Max(hi, Dist(i, j));
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
