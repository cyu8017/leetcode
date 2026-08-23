// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int numberOfWays(int n, int x) {
        final int MOD = 1_000_000_007;
        List<Integer> powers = new ArrayList<>();
        for (int i = 1; ; i++) {
            long p = 1;
            for (int j = 0; j < x; j++) {
                p *= i;
                if (p > n) break;
            }
            if (p > n) break;
            powers.add((int) p);
        }
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int p : powers) {
            for (int s = n; s >= p; s--)
                dp[s] = (dp[s] + dp[s - p]) % MOD;
        }
        return dp[n];
    }
}
