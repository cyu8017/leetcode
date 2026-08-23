// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

using System;
using System.Collections.Generic;

public class Solution {
    struct MarkNode {
        public int node;
        public int time;
        public MarkNode(int node, int time) { this.node = node; this.time = time; }
    }
    struct Top2 {
        public MarkNode top1;
        public MarkNode top2;
    }

    public int[] TimeTaken(int[][] edges) {
        int n = edges.Length + 1;
        int[] ans = new int[n];
        var tree = new List<int>[n];
        for (int i = 0; i < n; i++) tree[i] = new List<int>();
        var dp = new Top2[n];
        foreach (var e in edges) {
            tree[e[0]].Add(e[1]);
            tree[e[1]].Add(e[0]);
        }
        int GetTime(int u) => u % 2 == 0 ? 2 : 1;
        int Dfs(int u, int prev) {
            MarkNode t1 = new MarkNode(), t2 = new MarkNode();
            foreach (int v in tree[u]) {
                if (v == prev) continue;
                int t = Dfs(v, u) + GetTime(v);
                if (t >= t1.time) {
                    t2 = t1;
                    t1 = new MarkNode(v, t);
                } else if (t > t2.time) {
                    t2 = new MarkNode(v, t);
                }
            }
            dp[u] = new Top2 { top1 = t1, top2 = t2 };
            return t1.time;
        }
        void Reroot(int u, int prev, int maxTime) {
            ans[u] = maxTime;
            if (dp[u].top1.time > ans[u]) ans[u] = dp[u].top1.time;
            foreach (int v in tree[u]) {
                if (v == prev) continue;
                int side = dp[u].top1.time;
                if (dp[u].top1.node == v) side = dp[u].top2.time;
                int newMax = Math.Max(maxTime, side);
                Reroot(v, u, GetTime(u) + newMax);
            }
        }
        Dfs(0, -1);
        Reroot(0, -1, 0);
        return ans;
    }
}
