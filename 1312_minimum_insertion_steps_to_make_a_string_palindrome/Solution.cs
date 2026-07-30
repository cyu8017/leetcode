// LeetCode 1312 - Minimum Insertion Steps To Make A String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

public class Solution {
    public int MinInsertions(string s) {
        int n = s.Length;
        var dp = new int[n];
        for (int left = n - 2; left >= 0; left--) {
            int diagonal = 0;
            for (int right = left + 1; right < n; right++) {
                int old = dp[right];
                if (s[left] == s[right]) dp[right] = diagonal;
                else dp[right] = 1 + System.Math.Min(dp[right], dp[right - 1]);
                diagonal = old;
            }
        }
        return n == 0 ? 0 : dp[n - 1];
    }
}
