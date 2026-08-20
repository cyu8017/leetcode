// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

function longestCommonSubsequence(text1: string, text2: string): number {
    const m = text1.length, n = text2.length;
    const dp = Array(n + 1).fill(0);
    for (let i = 1; i <= m; i++) {
        let prev = 0;
        for (let j = 1; j <= n; j++) {
            const cur = dp[j];
            if (text1[i - 1] === text2[j - 1]) dp[j] = prev + 1;
            else dp[j] = Math.max(dp[j], dp[j - 1]);
            prev = cur;
        }
    }
    return dp[n];
}
