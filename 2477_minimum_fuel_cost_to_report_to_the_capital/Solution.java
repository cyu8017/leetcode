// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private long ans;
    private int seats;

    private int dfs(int u, int p) {
        int people = 1;
        for (int v : g[u]) {
            if (v != p) people += dfs(v, u);
        }
        if (u != 0) ans += (people + seats - 1) / seats;
        return people;
    }

    public long minimumFuelCost(int[][] roads, int seats) {
        this.seats = seats;
        int n = roads.length + 1;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] r : roads) {
            g[r[0]].add(r[1]);
            g[r[1]].add(r[0]);
        }
        ans = 0;
        dfs(0, -1);
        return ans;
    }
}
