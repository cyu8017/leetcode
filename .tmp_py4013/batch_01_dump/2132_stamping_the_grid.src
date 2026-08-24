// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

/**
 * @param {number[][]} grid
 * @param {number} stampHeight
 * @param {number} stampWidth
 * @return {boolean}
 */
var possibleToStamp = function(grid, stampHeight, stampWidth) {
    const m = grid.length, n = grid[0].length;
    const pref = Array.from({length: m + 1}, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j];
    const diff = Array.from({length: m + 1}, () => new Array(n + 1).fill(0));
    for (let i = 0; i + stampHeight - 1 < m; i++) {
        for (let j = 0; j + stampWidth - 1 < n; j++) {
            const sum = pref[i + stampHeight][j + stampWidth] - pref[i][j + stampWidth]
                    - pref[i + stampHeight][j] + pref[i][j];
            if (sum === 0) {
                diff[i][j]++;
                diff[i][j + stampWidth]--;
                diff[i + stampHeight][j]--;
                diff[i + stampHeight][j + stampWidth]++;
            }
        }
    }
    const cur = Array.from({length: m}, () => new Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let v = diff[i][j];
            if (i > 0) v += cur[i - 1][j];
            if (j > 0) v += cur[i][j - 1];
            if (i > 0 && j > 0) v -= cur[i - 1][j - 1];
            cur[i][j] = v;
            if (grid[i][j] === 0 && v === 0) return false;
        }
    }
    return true;
};
