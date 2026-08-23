// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static class MarkNode {
        int node;
        int time;
        MarkNode() {}
        MarkNode(int node, int time) { this.node = node; this.time = time; }
    }
    private static class Top2 {
        MarkNode top1 = new MarkNode();
        MarkNode top2 = new MarkNode();
    }

    private List<Integer>[] tree;
    private Top2[] dp;
    private int[] ans;

    public int[] timeTaken(int[][] edges) {
        int n = edges.length + 1;
        ans = new int[n];
        @SuppressWarnings("unchecked")
        List<Integer>[] tr = new ArrayList[n];
        for (int i = 0; i < n; i++) tr[i] = new ArrayList<>();
        tree = tr;
        dp = new Top2[n];
        for (int i = 0; i < n; i++) dp[i] = new Top2();
        for (int[] e : edges) {
            tree[e[0]].add(e[1]);
            tree[e[1]].add(e[0]);
        }
        dfs(0, -1);
        reroot(0, -1, 0);
        return ans;
    }

    private int getTime(int u) { return u % 2 == 0 ? 2 : 1; }

    private int dfs(int u, int prev) {
        MarkNode t1 = new MarkNode(), t2 = new MarkNode();
        for (int v : tree[u]) {
            if (v == prev) continue;
            int t = dfs(v, u) + getTime(v);
            if (t >= t1.time) {
                t2 = t1;
                t1 = new MarkNode(v, t);
            } else if (t > t2.time) {
                t2 = new MarkNode(v, t);
            }
        }
        dp[u].top1 = t1;
        dp[u].top2 = t2;
        return t1.time;
    }

    private void reroot(int u, int prev, int maxTime) {
        ans[u] = maxTime;
        if (dp[u].top1.time > ans[u]) ans[u] = dp[u].top1.time;
        for (int v : tree[u]) {
            if (v == prev) continue;
            int side = dp[u].top1.time;
            if (dp[u].top1.node == v) side = dp[u].top2.time;
            int newMax = Math.max(maxTime, side);
            reroot(v, u, getTime(u) + newMax);
        }
    }
}
