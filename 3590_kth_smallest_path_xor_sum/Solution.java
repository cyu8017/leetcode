// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    List<Integer>[] g;
    int[] xorPath, vals;
    int[] inT, outT;
    List<Integer> order;

    void dfs(int u) {
        xorPath[u] ^= vals[u];
        for (int v : g[u]) {
            xorPath[v] = xorPath[u];
            dfs(v);
        }
    }

    void dfs2(int u) {
        inT[u] = order.size();
        order.add(xorPath[u]);
        for (int v : g[u]) dfs2(v);
        outT[u] = order.size();
    }

    public int[] kthSmallest(int[] par, int[] vals, int[][] queries) {
        int n = par.length;
        this.vals = vals;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) g[par[i]].add(i);
        xorPath = new int[n];
        dfs(0);
        inT = new int[n];
        outT = new int[n];
        order = new ArrayList<>();
        dfs2(0);
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0], k = queries[i][1];
            List<Integer> sub = new ArrayList<>(order.subList(inT[u], outT[u]));
            Collections.sort(sub);
            List<Integer> uniq = new ArrayList<>();
            for (int x : sub) if (uniq.isEmpty() || uniq.get(uniq.size() - 1) != x) uniq.add(x);
            ans[i] = k > uniq.size() ? -1 : uniq.get(k - 1);
        }
        return ans;
    }
}
