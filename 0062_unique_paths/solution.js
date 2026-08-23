// LeetCode 0062 - Unique Paths
// https://leetcode.com/problems/unique-paths/

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const row = new Array(n).fill(1);

    for (let r = 1; r < m; r++) {
        for (let col = 1; col < n; col++) {
            row[col] += row[col - 1];
        }
    }

    return row[n - 1];
};
