// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

class Solution {
    public int longestIdealString(String s, int k) {
        int[] dp = new int[26];
        int ans = 0;
        for (char ch : s) {
            int c = ch - 'a';
            int best = 0;
            for (int p = 0; p < 26; p++)
                if (Math.abs(c - p) <= k && dp[p] > best) best = dp[p];
            dp[c] = best + 1;
            ans = Math.max(ans, dp[c]);
        }
        return ans;
    }
}
