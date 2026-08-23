// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

import java.util.TreeMap;

class Solution {
    public int countPartitions(int[] nums, int k) {
        final int mod = 1_000_000_007;
        TreeMap<Integer, Integer> sl = new TreeMap<>();
        int n = nums.length;
        int[] f = new int[n + 1], g = new int[n + 1];
        f[0] = g[0] = 1;
        for (int l = 1, r = 1; r <= n; r++) {
            sl.merge(nums[r - 1], 1, Integer::sum);
            while (sl.lastKey() - sl.firstKey() > k) {
                int v = nums[l - 1];
                int c = sl.get(v);
                if (c == 1) sl.remove(v);
                else sl.put(v, c - 1);
                l++;
            }
            f[r] = g[r - 1];
            if (l >= 2) f[r] = (f[r] - g[l - 2] + mod) % mod;
            g[r] = (g[r - 1] + f[r]) % mod;
        }
        return f[n];
    }
}
