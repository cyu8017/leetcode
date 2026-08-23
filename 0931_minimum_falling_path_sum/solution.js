// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function(matrix) {
    const n = matrix.length;
    let dp = matrix[0].slice();
    for (let i = 1; i < n; i++) {
        const next = new Array(n);
        for (let j = 0; j < n; j++) {
            let best = dp[j];
            if (j > 0) best = Math.min(best, dp[j - 1]);
            if (j + 1 < n) best = Math.min(best, dp[j + 1]);
            next[j] = matrix[i][j] + best;
        }
        dp = next;
    }
    return Math.min(...dp);
};
