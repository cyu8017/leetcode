// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

using System.Collections.Generic;

public class Solution {
    public int CountPartitions(int[] nums, int k) {
        const int mod = 1000000007;
        var sl = new SortedDictionary<int, int>();
        int n = nums.Length;
        int[] f = new int[n + 1], g = new int[n + 1];
        f[0] = g[0] = 1;
        void Add(int x) {
            if (!sl.ContainsKey(x)) sl[x] = 0;
            sl[x]++;
        }
        void Remove(int x) {
            if (--sl[x] == 0) sl.Remove(x);
        }
        int Min() { foreach (var kv in sl) return kv.Key; return 0; }
        int Max() {
            int m = 0;
            foreach (var kv in sl) m = kv.Key;
            return m;
        }
        for (int l = 1, r = 1; r <= n; r++) {
            Add(nums[r - 1]);
            while (Max() - Min() > k) {
                Remove(nums[l - 1]);
                l++;
            }
            f[r] = g[r - 1];
            if (l >= 2) f[r] = (f[r] - g[l - 2] + mod) % mod;
            g[r] = (g[r - 1] + f[r]) % mod;
        }
        return f[n];
    }
}
