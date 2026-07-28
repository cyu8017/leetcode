// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxEqualRowsAfterFlips = function(matrix) {
    const patterns = new Map();
    for (const row of matrix) {
        const base = row[0];
        const key = row.map((x) => x ^ base).join(",");
        patterns.set(key, (patterns.get(key) || 0) + 1);
    }
    return Math.max(...patterns.values());
};
