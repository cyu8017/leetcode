// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

class Solution {
    public boolean isValidPalindrome(String s, int k) {
        int n = s.length();
        int[] dp = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int previous = 0;
            for (int j = i + 1; j < n; j++) {
                int old = dp[j];
                if (s.charAt(i) == s.charAt(j)) dp[j] = previous;
                else dp[j] = 1 + Math.min(dp[j], dp[j - 1]);
                previous = old;
            }
        }
        return n == 0 || dp[n - 1] <= k;
    }
}
