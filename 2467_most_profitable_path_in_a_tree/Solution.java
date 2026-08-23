// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int[] amount, bobTime;
    private int ans;

    private boolean findBob(int u, int p, int t) {
        if (u == 0) {
            bobTime[u] = t;
            return true;
        }
        for (int v : g[u]) {
            if (v == p) continue;
            if (findBob(v, u, t + 1)) {
                bobTime[u] = t;
                return true;
            }
        }
        return false;
    }

    private void dfs(int u, int p, int t, int income) {
        int cur = amount[u];
        if (t > bobTime[u]) cur = 0;
        else if (t == bobTime[u]) cur /= 2;
        income += cur;
        boolean isLeaf = true;
        for (int v : g[u]) {
            if (v != p) {
                isLeaf = false;
                dfs(v, u, t + 1, income);
            }
        }
        if (isLeaf && income > ans) ans = income;
    }

    public int mostProfitablePath(int[][] edges, int bob, int[] amount) {
        this.amount = amount;
        int n = amount.length;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        bobTime = new int[n];
        Arrays.fill(bobTime, n);
        findBob(bob, -1, 0);
        ans = Integer.MIN_VALUE;
        dfs(0, -1, 0, 0);
        return ans;
    }
}
