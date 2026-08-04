// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

import java.util.*;

class Solution {
    public int minimumCost(int n, int[][] connections) {
        int[] parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        Arrays.sort(connections, (a, b) -> Integer.compare(a[2], b[2]));
        int cost = 0, edges = 0;
        for (int[] e : connections) {
            if (union(parent, e[0], e[1])) {
                cost += e[2];
                edges++;
                if (edges == n - 1) return cost;
            }
        }
        return -1;
    }

    private int find(int[] parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private boolean union(int[] parent, int a, int b) {
        int ra = find(parent, a), rb = find(parent, b);
        if (ra == rb) return false;
        parent[rb] = ra;
        return true;
    }
}
