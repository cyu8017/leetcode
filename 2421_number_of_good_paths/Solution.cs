// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

using System;
using System.Collections.Generic;

public class Solution {
    public int NumberOfGoodPaths(int[] vals, int[][] edges) {
        int n = vals.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int[] parent = new int[n], size = new int[n];
        for (int i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }
        int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        int[] nodes = new int[n];
        for (int i = 0; i < n; i++) nodes[i] = i;
        Array.Sort(nodes, (a, b) => vals[a].CompareTo(vals[b]));
        int ans = n;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && vals[nodes[j]] == vals[nodes[i]]) j++;
            for (int k = i; k < j; k++) {
                int u = nodes[k];
                foreach (int v in g[u]) {
                    if (vals[v] <= vals[u]) {
                        int ru = Find(u), rv = Find(v);
                        if (ru != rv) {
                            parent[ru] = rv;
                            size[rv] += size[ru];
                        }
                    }
                }
            }
            var freq = new Dictionary<int, int>();
            for (int k = i; k < j; k++) {
                int r = Find(nodes[k]);
                if (!freq.ContainsKey(r)) freq[r] = 0;
                freq[r]++;
            }
            foreach (var c in freq.Values) ans += c * (c - 1) / 2;
            i = j;
        }
        return ans;
    }
}
