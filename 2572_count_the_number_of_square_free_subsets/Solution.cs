// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

using System.Collections.Generic;

public class Solution {
    public int SquareFreeSubsets(int[] nums) {
        const int MOD = 1000000007;
        int[] primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 };
        int MaskOf(int x) {
            int mask = 0;
            for (int i = 0; i < primes.Length; ++i) {
                int p = primes[i], cnt = 0;
                while (x % p == 0) {
                    x /= p;
                    cnt++;
                    if (cnt > 1) return -1;
                }
                if (cnt == 1) mask |= 1 << i;
            }
            return mask;
        }
        var freq = new Dictionary<int, int>();
        foreach (int x in nums) freq[x] = freq.GetValueOrDefault(x, 0) + 1;
        int[] dp = new int[1 << 10];
        dp[0] = 1;
        foreach (var kv in freq) {
            int x = kv.Key, c = kv.Value;
            if (x == 1) continue;
            int m = MaskOf(x);
            if (m < 0) continue;
            for (int state = (1 << 10) - 1; state >= 0; --state) {
                if ((state & m) == 0) {
                    dp[state | m] = (int)((dp[state | m] + (long)dp[state] * c) % MOD);
                }
            }
        }
        int ans = 0;
        foreach (int v in dp) ans = (ans + v) % MOD;
        int ones = freq.GetValueOrDefault(1, 0);
        int mul = 1;
        for (int i = 0; i < ones; ++i) mul = mul * 2 % MOD;
        ans = (int)((long)ans * mul % MOD);
        ans = (ans - 1 + MOD) % MOD;
        return ans;
    }
}
