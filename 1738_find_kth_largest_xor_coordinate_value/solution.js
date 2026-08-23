// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthLargestValue = function(matrix, k) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    const pref = Array.from({ length: rows + 1 }, () => new Array(cols + 1).fill(0));
    const values = [];
    for (let r = 1; r <= rows; r++) {
        for (let c = 1; c <= cols; c++) {
            pref[r][c] = pref[r - 1][c] ^ pref[r][c - 1] ^ pref[r - 1][c - 1] ^ matrix[r - 1][c - 1];
            values.push(pref[r][c]);
        }
    }
    values.sort((x, y) => y - x);
    return values[k - 1];
};
