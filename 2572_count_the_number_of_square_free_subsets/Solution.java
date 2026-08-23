// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final int MOD = 1_000_000_007;
    private static final int[] PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

    public int squareFreeSubsets(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);
        int[] dp = new int[1 << 10];
        dp[0] = 1;
        for (Map.Entry<Integer, Integer> kv : freq.entrySet()) {
            int x = kv.getKey(), c = kv.getValue();
            if (x == 1) continue;
            int m = maskOf(x);
            if (m < 0) continue;
            for (int state = (1 << 10) - 1; state >= 0; --state) {
                if ((state & m) == 0) {
                    dp[state | m] = (int) ((dp[state | m] + (long) dp[state] * c) % MOD);
                }
            }
        }
        int ans = 0;
        for (int v : dp) ans = (ans + v) % MOD;
        int ones = freq.getOrDefault(1, 0);
        int mul = 1;
        for (int i = 0; i < ones; ++i) mul = mul * 2 % MOD;
        ans = (int) ((long) ans * mul % MOD);
        ans = (ans - 1 + MOD) % MOD;
        return ans;
    }

    private int maskOf(int x) {
        int mask = 0;
        for (int i = 0; i < PRIMES.length; ++i) {
            int p = PRIMES[i], cnt = 0;
            while (x % p == 0) {
                x /= p;
                cnt++;
                if (cnt > 1) return -1;
            }
            if (cnt == 1) mask |= 1 << i;
        }
        return mask;
    }
}
