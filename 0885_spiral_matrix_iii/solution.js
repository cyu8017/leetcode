// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

/**
 * @param {number} rows
 * @param {number} cols
 * @param {number} rStart
 * @param {number} cStart
 * @return {number[][]}
 */
var spiralMatrixIII = function(rows, cols, rStart, cStart) {
    const ans = [[rStart, cStart]];
    if (rows * cols === 1) return ans;
    let r = rStart, c = cStart;
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let steps = 1;
    while (ans.length < rows * cols) {
        for (let d = 0; d < 4; d++) {
            const [dr, dc] = dirs[d];
            for (let i = 0; i < steps; i++) {
                r += dr;
                c += dc;
                if (r >= 0 && r < rows && c >= 0 && c < cols) {
                    ans.push([r, c]);
                    if (ans.length === rows * cols) return ans;
                }
            }
            if (d % 2 === 1) steps++;
        }
    }
    return ans;
};
