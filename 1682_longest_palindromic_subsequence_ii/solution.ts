// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

function longestPalindromeSubseq(s: string): number {
    const n = s.length;
    const dp = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => Array(26).fill(0))
    );
    for (let length = 2; length <= n; length++) {
        for (let i = 0; i <= n - length; i++) {
            const j = i + length - 1;
            for (let c = 0; c < 26; c++) {
                dp[i][j][c] = Math.max(dp[i + 1][j][c], dp[i][j - 1][c]);
            }
            if (s[i] === s[j]) {
                const c = s.charCodeAt(i) - 97;
                let inner = 0;
                if (length > 2) {
                    for (let x = 0; x < 26; x++) {
                        if (x !== c) inner = Math.max(inner, dp[i + 1][j - 1][x]);
                    }
                }
                dp[i][j][c] = Math.max(dp[i][j][c], inner + 2);
            }
        }
    }
    return Math.max(...dp[0][n - 1]);
}
