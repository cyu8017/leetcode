// LeetCode 2133 - Check if Every Row and Column Contains All Numbers
// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var checkValid = function(matrix) {
    const n = matrix.length;
    for (let i = 0; i < n; i++) {
        const row = new Array(n + 1).fill(false), col = new Array(n + 1).fill(false);
        for (let j = 0; j < n; j++) {
            if (row[matrix[i][j]] || col[matrix[j][i]]) return false;
            row[matrix[i][j]] = col[matrix[j][i]] = true;
        }
    }
    return true;
};
