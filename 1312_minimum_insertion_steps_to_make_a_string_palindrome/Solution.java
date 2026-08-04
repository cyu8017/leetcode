// LeetCode 1312 - Minimum Insertion Steps To Make A String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution {
    public int minInsertions(String s) {
        int n = s.length();
        int[] dp = new int[n];
        for (int left = n - 2; left >= 0; left--) {
            int diagonal = 0;
            for (int right = left + 1; right < n; right++) {
                int old = dp[right];
                if (s.charAt(left) == s.charAt(right)) {
                    dp[right] = diagonal;
                } else {
                    dp[right] = 1 + Math.min(dp[right], dp[right - 1]);
                }
                diagonal = old;
            }
        }
        return n == 0 ? 0 : dp[n - 1];
    }
}
