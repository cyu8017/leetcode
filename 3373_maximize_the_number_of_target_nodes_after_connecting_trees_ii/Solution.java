// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
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

    private int[] bipartiteCount(List<Integer>[] g, int[] color) {
        Arrays.fill(color, -1);
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(0);
        color[0] = 0;
        int[] cnt = {1, 0};
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : g[u]) {
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    cnt[color[v]]++;
                    q.offer(v);
                }
            }
        }
        return cnt;
    }

    public int[] maxTargetNodes(int[][] edges1, int[][] edges2) {
        int n = edges1.length + 1;
        int m = edges2.length + 1;
        List<Integer>[] g1 = buildTree(n, edges1);
        List<Integer>[] g2 = buildTree(m, edges2);
        int[] color1 = new int[n], color2 = new int[m];
        int[] c1 = bipartiteCount(g1, color1);
        int[] c2 = bipartiteCount(g2, color2);
        int best2 = Math.max(c2[0], c2[1]);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = c1[color1[i]] + best2;
        return ans;
    }
}
