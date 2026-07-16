// LeetCode 0096 - Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    var dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    for (var nodes = 1; nodes <= n; nodes++) {
        for (var root = 1; root <= nodes; root++) {
            dp[nodes] += dp[root - 1] * dp[nodes - root];
        }
    }
    return dp[n];
};
