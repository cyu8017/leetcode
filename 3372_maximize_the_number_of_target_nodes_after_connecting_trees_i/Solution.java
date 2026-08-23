// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    private List<Integer>[] buildTree(int n, int[][] edges) {
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        return g;
    }

    private int countWithin(List<Integer>[] g, int start, int k) {
        if (k < 0) return 0;
        int n = g.length;
        boolean[] vis = new boolean[n];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {start, 0});
        vis[start] = true;
        int cnt = 0;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int u = cur[0], d = cur[1];
            cnt++;
            if (d == k) continue;
            for (int v : g[u]) {
                if (!vis[v]) {
                    vis[v] = true;
                    q.offer(new int[] {v, d + 1});
                }
            }
        }
        return cnt;
    }

    public int[] maxTargetNodes(int[][] edges1, int[][] edges2, int k) {
        int n = edges1.length + 1;
        int m = edges2.length + 1;
        List<Integer>[] g1 = buildTree(n, edges1);
        List<Integer>[] g2 = buildTree(m, edges2);
        int[] cnt1 = new int[n];
        for (int i = 0; i < n; i++) cnt1[i] = countWithin(g1, i, k);
        int best2 = 0;
        if (k > 0) {
            for (int i = 0; i < m; i++) {
                int c = countWithin(g2, i, k - 1);
                if (c > best2) best2 = c;
            }
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = cnt1[i] + best2;
        return ans;
    }
}
