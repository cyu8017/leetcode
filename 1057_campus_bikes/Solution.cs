// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] AssignBikes(int[][] workers, int[][] bikes) {
        var triples = new List<(int dist, int w, int b)>();
        for (int w = 0; w < workers.Length; w++) {
            for (int b = 0; b < bikes.Length; b++) {
                int dist = Math.Abs(workers[w][0] - bikes[b][0]) + Math.Abs(workers[w][1] - bikes[b][1]);
                triples.Add((dist, w, b));
            }
        }
        triples.Sort((a, b) => {
            int cmp = a.dist.CompareTo(b.dist);
            if (cmp != 0) return cmp;
            cmp = a.w.CompareTo(b.w);
            return cmp != 0 ? cmp : a.b.CompareTo(b.b);
        });
        int[] ans = new int[workers.Length];
        Array.Fill(ans, -1);
        var usedBikes = new HashSet<int>();
        int assigned = 0;
        foreach (var t in triples) {
            if (ans[t.w] == -1 && !usedBikes.Contains(t.b)) {
                ans[t.w] = t.b;
                usedBikes.Add(t.b);
                assigned++;
                if (assigned == workers.Length) {
                    break;
                }
            }
        }
        return ans;
    }
}
