// LeetCode 1582 - Special Positions in a Binary Matrix
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/

/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSpecial = function(mat) {
    const rows = mat.map((row) => row.reduce((a, b) => a + b, 0));
    const cols = Array(mat[0].length).fill(0);
    for (let j = 0; j < mat[0].length; j++) {
        for (let i = 0; i < mat.length; i++) cols[j] += mat[i][j];
    }
    let ans = 0;
    for (let i = 0; i < mat.length; i++) {
        for (let j = 0; j < mat[0].length; j++) {
            if (mat[i][j] === 1 && rows[i] === 1 && cols[j] === 1) ans++;
        }
    }
    return ans;
};
