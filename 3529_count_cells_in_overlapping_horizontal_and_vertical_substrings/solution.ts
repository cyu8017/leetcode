// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

export function countCells(grid: any, pattern: any): any {
    const m = grid.length, n = grid[0].length;
    let row = '', col = '';
    for (let i = 0; i < m; i++) for (let j = 0; j < n; j++) row += grid[i][j];
    for (let j = 0; j < n; j++) for (let i = 0; i < m; i++) col += grid[i][j];
    const hMark = Array.from({length: m}, () => new Array(n).fill(false));
    const vMark = Array.from({length: m}, () => new Array(n).fill(false));
    const plen = pattern.length;
    for (let i = 0; i + plen <= row.length; i++) {
        if (row.substring(i, i + plen) === pattern) {
            for (let t = 0; t < plen; t++) {
                const pos = i + t;
                hMark[Math.floor(pos / n)][pos % n] = true;
            }
        }
    }
    for (let i = 0; i + plen <= col.length; i++) {
        if (col.substring(i, i + plen) === pattern) {
            for (let t = 0; t < plen; t++) {
                const pos = i + t;
                vMark[pos % m][Math.floor(pos / m)] = true;
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < m; i++) for (let j = 0; j < n; j++)
        if (hMark[i][j] && vMark[i][j]) ans++;
    return ans;
}
