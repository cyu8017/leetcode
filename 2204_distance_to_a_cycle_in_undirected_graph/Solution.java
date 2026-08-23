// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int[] distanceToCycle(int n, int[][] edges) {
        @SuppressWarnings("unchecked")
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        int[] deg = new int[n];
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
            deg[e[0]]++;
            deg[e[1]]++;
        }
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (deg[i] == 1) q.offer(i);
        boolean[] onCycle = new boolean[n];
        for (int i = 0; i < n; i++) onCycle[i] = true;
        while (!q.isEmpty()) {
            int u = q.poll();
            onCycle[u] = false;
            for (int v : g[u]) {
                if (--deg[v] == 1) q.offer(v);
            }
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = -1;
        Queue<Integer> qq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (onCycle[i]) {
            ans[i] = 0;
            qq.offer(i);
        }
        while (!qq.isEmpty()) {
            int u = qq.poll();
            for (int v : g[u]) if (ans[v] == -1) {
                ans[v] = ans[u] + 1;
                qq.offer(v);
            }
        }
        return ans;
    }
}
