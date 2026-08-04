// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

class Solution {
    public int numberOfGoodSubsets(int[] nums) {
        final int MOD = 1_000_000_007;
        int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        int[] masks = new int[31];
        for (int x = 2; x <= 30; x++) {
            int m = 0, y = x;
            boolean ok = true;
            for (int i = 0; i < primes.length; i++) {
                int p = primes[i];
                if (y % p == 0) {
                    if ((y / p) % p == 0) { ok = false; break; }
                    m |= 1 << i;
                    y /= p;
                }
            }
            masks[x] = ok ? m : -1;
        }
        int[] cnt = new int[31];
        for (int v : nums) cnt[v]++;
        long[] dp = new long[1 << primes.length];
        dp[0] = 1;
        for (int x = 2; x <= 30; x++) {
            if (cnt[x] == 0 || masks[x] < 0) continue;
            int m = masks[x];
            for (int state = (1 << primes.length) - 1; state >= 0; state--) {
                if ((state & m) != 0) continue;
                dp[state | m] = (dp[state | m] + dp[state] * cnt[x]) % MOD;
            }
        }
        long ans = 0;
        for (int i = 1; i < dp.length; i++) ans = (ans + dp[i]) % MOD;
        long mul = 1;
        for (int i = 0; i < cnt[1]; i++) mul = mul * 2 % MOD;
        return (int) (ans * mul % MOD);
    }
}
