// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

import java.util.*;

class Solution {
    public List<Boolean> areConnected(int n, int threshold, int[][] queries) {
        int[] parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        for (int d = threshold + 1; d <= n; d++) {
            for (int x = 2 * d; x <= n; x += d) {
                union(parent, d, x);
            }
        }
        List<Boolean> ans = new ArrayList<>();
        for (int[] q : queries) {
            ans.add(find(parent, q[0]) == find(parent, q[1]));
        }
        return ans;
    }

    private int find(int[] parent, int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int[] parent, int a, int b) {
        int pa = find(parent, a), pb = find(parent, b);
        if (pa != pb) parent[pb] = pa;
    }
}
