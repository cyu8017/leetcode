// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxTrailingZeros = function(grid) {
    const fact = (x) => {
        let t = 0, f = 0;
        while (x % 2 === 0) { t++; x = Math.floor(x / 2); }
        while (x % 5 === 0) { f++; x = Math.floor(x / 5); }
        return [t, f];
    };
    const m = grid.length, n = grid[0].length;
    const left2 = Array.from({length: m}, () => new Array(n).fill(0));
    const left5 = Array.from({length: m}, () => new Array(n).fill(0));
    const up2 = Array.from({length: m}, () => new Array(n).fill(0));
    const up5 = Array.from({length: m}, () => new Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const p = fact(grid[i][j]);
            left2[i][j] = up2[i][j] = p[0];
            left5[i][j] = up5[i][j] = p[1];
            if (j > 0) {
                left2[i][j] += left2[i][j - 1];
                left5[i][j] += left5[i][j - 1];
            }
            if (i > 0) {
                up2[i][j] += up2[i - 1][j];
                up5[i][j] += up5[i - 1][j];
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const cell = fact(grid[i][j]);
            const L2 = left2[i][j], L5 = left5[i][j];
            const R2 = left2[i][n - 1] - left2[i][j] + cell[0];
            const R5 = left5[i][n - 1] - left5[i][j] + cell[1];
            const U2 = up2[i][j], U5 = up5[i][j];
            const D2 = up2[m - 1][j] - up2[i][j] + cell[0];
            const D5 = up5[m - 1][j] - up5[i][j] + cell[1];
            const cands = [
                [L2 + U2 - cell[0], L5 + U5 - cell[1]],
                [L2 + D2 - cell[0], L5 + D5 - cell[1]],
                [R2 + U2 - cell[0], R5 + U5 - cell[1]],
                [R2 + D2 - cell[0], R5 + D5 - cell[1]],
            ];
            for (const [a, b] of cands) ans = Math.max(ans, Math.min(a, b));
        }
    }
    return ans;
};
