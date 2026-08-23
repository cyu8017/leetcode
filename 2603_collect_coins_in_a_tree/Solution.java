// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int collectTheCoins(int[] coins, int[][] edges) {
        int n = coins.length;
        Set<Integer>[] g = new HashSet[n];
        for (int i = 0; i < n; i++) g[i] = new HashSet<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int[] deg = new int[n];
        for (int i = 0; i < n; ++i) deg[i] = g[i].size();
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; ++i) {
            if (deg[i] == 1 && coins[i] == 0) q.offer(i);
        }
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : new ArrayList<>(g[u])) {
                g[v].remove(u);
                deg[v]--;
                if (deg[v] == 1 && coins[v] == 0) q.offer(v);
            }
            g[u].clear();
            deg[u] = 0;
        }
        for (int round = 0; round < 2; ++round) {
            List<Integer> leaves = new ArrayList<>();
            for (int i = 0; i < n; ++i) if (deg[i] == 1) leaves.add(i);
            for (int u : leaves) {
                for (int v : new ArrayList<>(g[u])) {
                    g[v].remove(u);
                    deg[v]--;
                }
                g[u].clear();
                deg[u] = 0;
            }
        }
        int remain = 0;
        for (int i = 0; i < n; ++i) remain += g[i].size();
        return remain;
    }
}
