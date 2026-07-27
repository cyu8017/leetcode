// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution {
    private static final int MOD = 1_000_000_007;

    public int numWays(String[] words, String target) {
        int m = words[0].length();
        long[] dp = new long[target.length() + 1];
        dp[0] = 1;
        for (int j = 0; j < m; j++) {
            int[] count = new int[26];
            for (String word : words) count[word.charAt(j) - 'a']++;
            for (int i = Math.min(j + 1, target.length()); i >= 1; i--) {
                dp[i] = (dp[i] + dp[i - 1] * count[target.charAt(i - 1) - 'a']) % MOD;
            }
        }
        return (int) dp[target.length()];
    }
}
