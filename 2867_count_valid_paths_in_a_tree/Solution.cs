// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

using System.Collections.Generic;

public class Solution {
    public long CountPaths(int n, int[][] edges) {
        bool[] isPrime = new bool[n + 1];
        for (int i = 0; i <= n; i++) isPrime[i] = true;
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) isPrime[j] = false;
            }
        }
        var g = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int Dfs(int u, int p) {
            if (isPrime[u]) return 0;
            int sz = 1;
            foreach (int v in g[u]) if (v != p) sz += Dfs(v, u);
            return sz;
        }
        long ans = 0;
        for (int u = 1; u <= n; u++) {
            if (!isPrime[u]) continue;
            long total = 0;
            foreach (int v in g[u]) {
                int c = Dfs(v, u);
                ans += c;
                ans += total * c;
                total += c;
            }
        }
        return ans;
    }
}
