// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

/**
 * @param {string} s
 * @return {number}
 */
var deleteString = function(s) {
    const n = s.length;
    const lcp = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));
    for (let i = n - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (s[i] === s[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1;
        }
    }
    const dp = Array(n);
    for (let i = n - 1; i >= 0; i--) {
        dp[i] = 1;
        for (let len = 1; i + 2 * len <= n; len++) {
            if (lcp[i][i + len] >= len) dp[i] = Math.max(dp[i], 1 + dp[i + len]);
        }
    }
    return dp[0];
};
