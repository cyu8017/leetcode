// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

public class Solution {
    int ModPow(long a, long e, int mod) {
        long r = 1;
        a %= mod;
        while (e > 0) {
            if ((e & 1) != 0) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return (int)r;
    }

    public int NumberOfWays(int n, int x, int y) {
        const int mod = 1000000007;
        int[][] dp = new int[n + 1][];
        for (int i = 0; i <= n; i++) dp[i] = new int[x + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= x && j <= i; j++) {
                dp[i][j] = (dp[i - 1][j - 1] + (int)((long)j * dp[i - 1][j] % mod)) % mod;
            }
        }
        int[] fact = new int[x + 1];
        fact[0] = 1;
        for (int i = 1; i <= x; i++) fact[i] = (int)((long)fact[i - 1] * i % mod);
        int ans = 0, ypow = 1;
        for (int k = 1; k <= x && k <= n; k++) {
            ypow = (int)((long)ypow * y % mod);
            int perm = (int)((long)fact[x] * ModPow(fact[x - k], mod - 2, mod) % mod);
            ans = (ans + (int)((long)dp[n][k] * perm % mod * ypow % mod)) % mod;
        }
        return ans;
    }
}
