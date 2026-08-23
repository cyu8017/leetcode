// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var getBiggestThree = function(grid) {
    const m = grid.length, n = grid[0].length;
    const s1 = Array.from({ length: m + 1 }, () => new Array(n + 2).fill(0));
    const s2 = Array.from({ length: m + 1 }, () => new Array(n + 2).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            s1[i][j] = s1[i - 1][j - 1] + grid[i - 1][j - 1];
            s2[i][j] = s2[i - 1][j + 1] + grid[i - 1][j - 1];
        }
    }
    const sums = new Set();
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            const limit = Math.min(i - 1, m - i, j - 1, n - j);
            sums.add(grid[i - 1][j - 1]);
            for (let k = 1; k <= limit; k++) {
                const a = s1[i + k][j] - s1[i][j - k];
                const b = s1[i][j + k] - s1[i - k][j];
                const c = s2[i][j - k] - s2[i - k][j];
                const d = s2[i + k][j] - s2[i][j + k];
                sums.add(a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]);
            }
        }
    }
    return [...sums].sort((a, b) => b - a).slice(0, 3);
};
