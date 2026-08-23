// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

/**
 * @param {string} s
 * @return {number}
 */
var strangePrinter = function(s) {
    const n = s.length;
    if (n === 0) return 0;
    const dp = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = n - 1; i >= 0; --i) {
        dp[i][i] = 1;
        for (let j = i + 1; j < n; ++j) {
            dp[i][j] = dp[i + 1][j] + 1;
            for (let k = i + 1; k <= j; ++k) {
                if (s[k] === s[i]) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k - 1] + (k + 1 <= j ? dp[k + 1][j] : 0));
                }
            }
        }
    }
    return dp[0][n - 1];
};
