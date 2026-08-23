// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

class Solution {
    public int numPermsDISequence(String s) {
        final int MOD = 1_000_000_007;
        int n = s.length();
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = 1;
        for (int i = 1; i <= n; i++) {
            int[] newDp = new int[n + 1];
            if (s.charAt(i - 1) == 'I') {
                int postfix = 0;
                for (int j = n - i; j >= 0; j--) {
                    postfix = (postfix + dp[j + 1]) % MOD;
                    newDp[j] = postfix;
                }
            } else {
                int prefix = 0;
                for (int j = 0; j <= n - i; j++) {
                    prefix = (prefix + dp[j]) % MOD;
                    newDp[j] = prefix;
                }
            }
            dp = newDp;
        }
        return dp[0];
    }
}
