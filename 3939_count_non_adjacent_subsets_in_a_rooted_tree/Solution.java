// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int countNonAdjacentSubsets(int[] parent, int[] nums, int k) {
        final long mod = 1000000007;
        int n = parent.length;
        List<Integer>[] children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) children[parent[i]].add(i);
        long[][] dp0 = new long[n][];
        long[][] dp1 = new long[n][];
        for (int u = n - 1; u >= 0; u--) {
            long[] a = new long[k], b = new long[k];
            a[0] = 1;
            b[((nums[u] % k) + k) % k] = 1;
            for (int v : children[u]) {
                long[] na = new long[k], nb = new long[k];
                for (int x = 0; x < k; x++) {
                    for (int y = 0; y < k; y++) {
                        long allChild = (dp0[v][y] + dp1[v][y]) % mod;
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * allChild) % mod;
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod;
                    }
                }
                a = na;
                b = nb;
            }
            dp0[u] = a;
            dp1[u] = b;
        }
        long ans = (dp0[0][0] + dp1[0][0] - 1) % mod;
        if (ans < 0) ans += mod;
        return (int) ans;
    }
}
