// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

using System.Collections.Generic;

public class Solution {
    public long SumOfAncestors(int n, int[][] edges, int[] nums) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            graph[e[0]].Add(e[1]);
            graph[e[1]].Add(e[0]);
        }
        int Kernel(int x) {
            int res = 1;
            for (int p = 2; p * p <= x; p++) {
                int cnt = 0;
                while (x % p == 0) { x /= p; cnt++; }
                if (cnt % 2 == 1) res *= p;
            }
            if (x > 1) res *= x;
            return res;
        }
        int[] ks = new int[n];
        for (int i = 0; i < n; i++) ks[i] = Kernel(nums[i]);
        var freq = new Dictionary<int, int>();
        long ans = 0;
        void Dfs(int u, int p) {
            if (!freq.ContainsKey(ks[u])) freq[ks[u]] = 0;
            ans += freq[ks[u]];
            freq[ks[u]]++;
            foreach (int v in graph[u]) if (v != p) Dfs(v, u);
            freq[ks[u]]--;
        }
        Dfs(0, -1);
        return ans;
    }
}
