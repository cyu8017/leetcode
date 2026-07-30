// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

public class Solution {
    public int NumberOfGoodSubsets(int[] nums) {
        const int MOD = 1000000007;
        int[] primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 };
        var masks = new int[31];
        for (int x = 2; x <= 30; x++) {
            int m = 0, y = x;
            bool ok = true;
            for (int i = 0; i < primes.Length; i++) {
                int p = primes[i];
                if (y % p == 0) {
                    if ((y / p) % p == 0) { ok = false; break; }
                    m |= 1 << i;
                    y /= p;
                }
            }
            masks[x] = ok ? m : -1;
        }
        var cnt = new int[31];
        foreach (int v in nums) cnt[v]++;
        int pcount = primes.Length;
        var dp = new long[1 << pcount];
        dp[0] = 1;
        for (int x = 2; x <= 30; x++) {
            if (cnt[x] == 0 || masks[x] < 0) continue;
            int m = masks[x];
            for (int state = (1 << pcount) - 1; state >= 0; state--) {
                if ((state & m) != 0) continue;
                dp[state | m] = (dp[state | m] + dp[state] * cnt[x]) % MOD;
            }
        }
        long ans = 0;
        for (int i = 1; i < dp.Length; i++) ans = (ans + dp[i]) % MOD;
        long pow2 = 1;
        for (int i = 0; i < cnt[1]; i++) pow2 = pow2 * 2 % MOD;
        return (int)(ans * pow2 % MOD);
    }
}