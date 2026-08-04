// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

import java.util.*;

class Solution {
    public double frogPosition(int n, int[][] edges, int t, int target) {
        List<List<Integer>> g = new ArrayList<>();
        for (int i = 0; i <= n; i++) g.add(new ArrayList<>());
        for (int[] e : edges) {
            g.get(e[0]).add(e[1]);
            g.get(e[1]).add(e[0]);
        }
        return dfs(1, 0, 0, 1.0, g, t, target);
    }

    private double dfs(int u, int p, int time, double prob, List<List<Integer>> g, int t, int target) {
        List<Integer> kids = new ArrayList<>();
        for (int v : g.get(u)) if (v != p) kids.add(v);
        if (time == t || kids.isEmpty()) return u == target ? prob : 0;
        double sum = 0;
        for (int v : kids) sum += dfs(v, u, time + 1, prob / kids.size(), g, t, target);
        return sum;
    }
}
