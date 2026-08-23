// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

using System.Collections.Generic;

public class Solution {
    public int CountNonAdjacentSubsets(int[] parent, int[] nums, int k) {
        const long mod = 1000000007;
        int n = parent.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) children[parent[i]].Add(i);
        var dp0 = new long[n][];
        var dp1 = new long[n][];
        for (int u = n - 1; u >= 0; u--) {
            long[] a = new long[k], b = new long[k];
            a[0] = 1;
            b[((nums[u] % k) + k) % k] = 1;
            foreach (int v in children[u]) {
                long[] na = new long[k], nb = new long[k];
                for (int x = 0; x < k; x++) {
                    for (int y = 0; y < k; y++) {
                        long allChild = (dp0[v][y] + dp1[v][y]) % mod;
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * allChild) % mod;
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod;
                    }
                }
                a = na; b = nb;
            }
            dp0[u] = a; dp1[u] = b;
        }
        long ans = (dp0[0][0] + dp1[0][0] - 1) % mod;
        if (ans < 0) ans += mod;
        return (int)ans;
    }
}
