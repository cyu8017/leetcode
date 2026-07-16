// LeetCode 0115 - Distinct Subsequences
// https://leetcode.com/problems/distinct-subsequences/

class Solution {
    public int numDistinct(String s, String t) {
        long[] dp = new long[t.length() + 1];
        dp[0] = 1;
        for (char ch : s.toCharArray()) {
            for (int j = t.length(); j >= 1; j--) {
                if (ch == t.charAt(j - 1)) dp[j] += dp[j - 1];
            }
        }
        return (int) dp[t.length()];
    }
}