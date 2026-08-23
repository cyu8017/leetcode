// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

public class Solution {
    public int KnightDialer(int n) {
        const int MOD = 1000000007;
        int[][] moves = new[] {
            new[] { 4, 6 }, new[] { 6, 8 }, new[] { 7, 9 }, new[] { 4, 8 }, new[] { 0, 3, 9 },
            new int[0], new[] { 0, 1, 7 }, new[] { 2, 6 }, new[] { 1, 3 }, new[] { 2, 4 }
        };
        long[] dp = new long[10];
        for (int i = 0; i < 10; i++) dp[i] = 1;
        for (int step = 0; step < n - 1; step++) {
            long[] ndp = new long[10];
            for (int i = 0; i < 10; i++)
                foreach (int j in moves[i]) ndp[j] = (ndp[j] + dp[i]) % MOD;
            dp = ndp;
        }
        long ans = 0;
        foreach (var x in dp) ans = (ans + x) % MOD;
        return (int)ans;
    }
}
