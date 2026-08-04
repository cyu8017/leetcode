// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

import java.util.*;

class Solution {
    public int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        int[] parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < wells.length; i++) edges.add(new int[]{0, i + 1, wells[i]});
        for (int[] p : pipes) edges.add(p);
        edges.sort((a, b) -> Integer.compare(a[2], b[2]));
        int ans = 0;
        for (int[] e : edges) {
            int ra = find(parent, e[0]), rb = find(parent, e[1]);
            if (ra == rb) continue;
            parent[rb] = ra;
            ans += e[2];
        }
        return ans;
    }
    private int find(int[] parent, int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
}
