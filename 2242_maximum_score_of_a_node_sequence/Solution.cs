// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumScore(int[] scores, int[][] edges) {
        int n = scores.Length;
        var top = new List<int>[n];
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) { top[i] = new List<int>(); g[i] = new List<int>(); }
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        for (int i = 0; i < n; i++) {
            foreach (int v in g[i]) {
                top[i].Add(v);
                for (int j = top[i].Count - 1; j > 0; j--) {
                    if (scores[top[i][j]] > scores[top[i][j - 1]]) {
                        int tmp = top[i][j]; top[i][j] = top[i][j - 1]; top[i][j - 1] = tmp;
                    }
                }
                if (top[i].Count > 3) top[i].RemoveRange(3, top[i].Count - 3);
            }
        }
        int ans = -1;
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            foreach (int c in top[a]) {
                if (c == b) continue;
                foreach (int d in top[b]) {
                    if (d == a || d == c) continue;
                    ans = Math.Max(ans, scores[a] + scores[b] + scores[c] + scores[d]);
                }
            }
        }
        return ans;
    }
}
