// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution {
    longestPalindromeSubseq(s) {
        const length = s.length;
        const dp = Array.from({ length }, () => Array(length).fill(0));
        for (let index = length - 1; index >= 0; index -= 1) {
            dp[index][index] = 1;
            for (let end = index + 1; end < length; end += 1) {
                if (s[index] === s[end]) dp[index][end] = dp[index + 1][end - 1] + 2;
                else dp[index][end] = Math.max(dp[index + 1][end], dp[index][end - 1]);
            }
        }
        return dp[0][length - 1];
    }
}

module.exports = { Solution };
