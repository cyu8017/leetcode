// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private int[] parent, size;

    private int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    public int numberOfGoodPaths(int[] vals, int[][] edges) {
        int n = vals.length;
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        parent = new int[n];
        size = new int[n];
        Arrays.fill(size, 1);
        for (int i = 0; i < n; i++) parent[i] = i;
        Integer[] nodes = new Integer[n];
        for (int i = 0; i < n; i++) nodes[i] = i;
        Arrays.sort(nodes, (a, b) -> Integer.compare(vals[a], vals[b]));
        int ans = n;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && vals[nodes[j]] == vals[nodes[i]]) j++;
            for (int k = i; k < j; k++) {
                int u = nodes[k];
                for (int v : g[u]) {
                    if (vals[v] <= vals[u]) {
                        int ru = find(u), rv = find(v);
                        if (ru != rv) {
                            parent[ru] = rv;
                            size[rv] += size[ru];
                        }
                    }
                }
            }
            Map<Integer, Integer> freq = new HashMap<>();
            for (int k = i; k < j; k++) {
                int r = find(nodes[k]);
                freq.put(r, freq.getOrDefault(r, 0) + 1);
            }
            for (int c : freq.values()) ans += c * (c - 1) / 2;
            i = j;
        }
        return ans;
    }
}
