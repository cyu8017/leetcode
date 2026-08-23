// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    if (!matrix || matrix.length === 0) {
        return 0;
    }
    const rows = matrix.length;
    const cols = matrix[0].length;
    const dp = new Array(cols + 1).fill(0);
    let maxSide = 0;
    let prev = 0;
    for (let row = 1; row <= rows; row += 1) {
        for (let col = 1; col <= cols; col += 1) {
            const temp = dp[col];
            if (matrix[row - 1][col - 1] === "1") {
                dp[col] = Math.min(dp[col], dp[col - 1], prev) + 1;
                maxSide = Math.max(maxSide, dp[col]);
            } else {
                dp[col] = 0;
            }
            prev = temp;
        }
    }
    return maxSide * maxSide;
};
