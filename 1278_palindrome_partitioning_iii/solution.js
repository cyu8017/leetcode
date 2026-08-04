// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var palindromePartition = function(s, k) {
    const n = s.length;
    const cost = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let length = 2; length <= n; length++) {
        for (let i = 0; i <= n - length; i++) {
            const j = i + length - 1;
            cost[i][j] = (length > 2 ? cost[i + 1][j - 1] : 0) + (s[i] !== s[j] ? 1 : 0);
        }
    }
    const inf = n + 1;
    const dp = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(inf));
    dp[0][0] = 0;
    for (let parts = 1; parts <= k; parts++) {
        for (let end = parts; end <= n; end++) {
            for (let start = parts - 1; start < end; start++) {
                dp[parts][end] = Math.min(dp[parts][end], dp[parts - 1][start] + cost[start][end - 1]);
            }
        }
    }
    return dp[k][n];
};
