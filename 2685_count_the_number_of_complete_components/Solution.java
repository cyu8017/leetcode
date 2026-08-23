// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

import java.util.*;

class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        List<Integer>[] g = new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        boolean[] vis = new boolean[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (vis[i]) continue;
            List<Integer> nodes = new ArrayList<>();
            dfs(g, vis, i, nodes);
            int ecount = 0;
            for (int u : nodes) ecount += g[u].size();
            ecount /= 2;
            int sz = nodes.size();
            if (ecount == sz * (sz - 1) / 2) ans++;
        }
        return ans;
    }

    private void dfs(List<Integer>[] g, boolean[] vis, int u, List<Integer> nodes) {
        vis[u] = true;
        nodes.add(u);
        for (int v : g[u]) if (!vis[v]) dfs(g, vis, v, nodes);
    }
}
