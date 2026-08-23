// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int reachableNodes(int n, int[][] edges, int[] restricted) {
        Set<Integer> ban = new HashSet<>();
        for (int x : restricted) ban.add(x);
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int ans = 0;
        boolean[] vis = new boolean[n];
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(0);
        vis[0] = true;
        while (!q.isEmpty()) {
            int u = q.poll();
            ans++;
            for (int v : g[u]) {
                if (!vis[v] && !ban.contains(v)) {
                    vis[v] = true;
                    q.offer(v);
                }
            }
        }
        return ans;
    }
}
