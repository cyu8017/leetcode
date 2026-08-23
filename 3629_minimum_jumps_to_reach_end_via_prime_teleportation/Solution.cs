// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

using System.Collections.Generic;

public class Solution {
    const int Mx = 1000001;
    static List<int>[] facCache;

    static List<int>[] Factors() {
        if (facCache == null) {
            facCache = new List<int>[Mx];
            for (int i = 0; i < Mx; i++) facCache[i] = new List<int>();
            for (int i = 2; i < Mx; i++) {
                if (facCache[i].Count == 0) {
                    for (int j = i; j < Mx; j += i) facCache[j].Add(i);
                }
            }
        }
        return facCache;
    }

    public int MinJumps(int[] nums) {
        var fac = Factors();
        int n = nums.Length;
        var g = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            foreach (int p in fac[nums[i]]) {
                if (!g.ContainsKey(p)) g[p] = new List<int>();
                g[p].Add(i);
            }
        }
        int ans = 0;
        bool[] vis = new bool[n];
        vis[0] = true;
        var q = new List<int> { 0 };
        while (true) {
            var nq = new List<int>();
            foreach (int i in q) {
                if (i == n - 1) return ans;
                var idx = g.ContainsKey(nums[i]) ? new List<int>(g[nums[i]]) : new List<int>();
                idx.Add(i + 1);
                if (i > 0) idx.Add(i - 1);
                foreach (int j in idx) {
                    if (j >= 0 && j < n && !vis[j]) {
                        vis[j] = true;
                        nq.Add(j);
                    }
                }
                if (g.ContainsKey(nums[i])) g[nums[i]].Clear();
            }
            q = nq;
            ans++;
        }
    }
}
