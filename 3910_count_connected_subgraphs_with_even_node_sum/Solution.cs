// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

using System.Collections.Generic;

public class Solution {
    public int EvenSumSubgraphs(int[] nums, int[][] edges) {
        int n = nums.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int m = (1 << n) - 1;
        int ans = 0;
        int vis = 0;

        void Dfs(int u) {
            vis |= 1 << u;
            foreach (int v in g[u]) {
                if (((vis >> v) & 1) == 0) Dfs(v);
            }
        }

        for (int sub = 1; sub <= m; sub++) {
            int s = 0;
            for (int i = 0; i < n; i++) {
                if (((sub >> i) & 1) != 0) s += nums[i];
            }
            if (s % 2 != 0) continue;
            vis = m ^ sub;
            int start = 31 - NumberOfLeadingZeros(sub);
            Dfs(start);
            if (vis == m) ans++;
        }
        return ans;
    }

    static int NumberOfLeadingZeros(int x) {
        if (x == 0) return 32;
        int n = 0;
        uint u = (uint)x;
        if (u <= 0x0000FFFF) { n += 16; u <<= 16; }
        if (u <= 0x00FFFFFF) { n += 8; u <<= 8; }
        if (u <= 0x0FFFFFFF) { n += 4; u <<= 4; }
        if (u <= 0x3FFFFFFF) { n += 2; u <<= 2; }
        if (u <= 0x7FFFFFFF) { n += 1; }
        return n;
    }
}
