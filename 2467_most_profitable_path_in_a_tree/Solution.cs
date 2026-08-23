// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

using System;
using System.Collections.Generic;

public class Solution {
    private List<int>[] g;
    private int[] bobTime, amount;
    private int ans;

    public int MostProfitablePath(int[][] edges, int bob, int[] amount) {
        this.amount = amount;
        int n = amount.Length;
        g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        bobTime = new int[n];
        for (int i = 0; i < n; i++) bobTime[i] = n;
        FindBob(bob, -1, 0);
        ans = int.MinValue;
        Dfs(0, -1, 0, 0);
        return ans;
    }

    private bool FindBob(int u, int p, int t) {
        if (u == 0) {
            bobTime[u] = t;
            return true;
        }
        foreach (int v in g[u]) {
            if (v == p) continue;
            if (FindBob(v, u, t + 1)) {
                bobTime[u] = t;
                return true;
            }
        }
        return false;
    }

    private void Dfs(int u, int p, int t, int income) {
        int cur = amount[u];
        if (t > bobTime[u]) cur = 0;
        else if (t == bobTime[u]) cur /= 2;
        income += cur;
        bool isLeaf = true;
        foreach (int v in g[u]) {
            if (v != p) {
                isLeaf = false;
                Dfs(v, u, t + 1, income);
            }
        }
        if (isLeaf && income > ans) ans = income;
    }
}
