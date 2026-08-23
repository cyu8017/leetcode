// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

class Solution {
    public int kInversePairs(int n, int k) {
        final int mod = 1000000007;
        int[] dp = new int[k + 1];
        dp[0] = 1;
        for (int size = 1; size <= n; ++size) {
            int[] nxt = new int[k + 1];
            long prefix = 0;
            for (int pairs = 0; pairs <= k; ++pairs) {
                prefix = (prefix + dp[pairs]) % mod;
                if (pairs >= size) {
                    prefix = (prefix - dp[pairs - size] + mod) % mod;
                }
                nxt[pairs] = (int) prefix;
            }
            dp = nxt;
        }
        return dp[k];
    }
}
