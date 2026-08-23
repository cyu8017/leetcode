// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

using System.Collections.Generic;

public class Solution {
    private List<int>[] g;
    private long ans;
    private int seats;

    public long MinimumFuelCost(int[][] roads, int seats) {
        this.seats = seats;
        int n = roads.Length + 1;
        g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var r in roads) {
            g[r[0]].Add(r[1]);
            g[r[1]].Add(r[0]);
        }
        ans = 0;
        Dfs(0, -1);
        return ans;
    }

    private int Dfs(int u, int p) {
        int people = 1;
        foreach (int v in g[u]) {
            if (v != p) people += Dfs(v, u);
        }
        if (u != 0) ans += (people + seats - 1) / seats;
        return people;
    }
}
