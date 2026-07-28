// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

/**
 * @param {number[][]} grid
 * @param {number} row
 * @param {number} col
 * @param {number} color
 * @return {number[][]}
 */
var colorBorder = function(grid, row, col, color) {
    const m = grid.length, n = grid[0].length;
    const original = grid[row][col];
    const component = new Set();
    const key = (r, c) => `${r},${c}`;
    const stack = [[row, col]];
    component.add(key(row, col));
    while (stack.length) {
        const [r, c] = stack.pop();
        for (const [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]) {
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] === original && !component.has(key(nr, nc))) {
                component.add(key(nr, nc));
                stack.push([nr, nc]);
            }
        }
    }
    const border = [];
    for (const item of component) {
        const [r, c] = item.split(',').map(Number);
        for (const [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]) {
            if (!(nr >= 0 && nr < m && nc >= 0 && nc < n) || !component.has(key(nr, nc))) {
                border.push([r, c]);
                break;
            }
        }
    }
    for (const [r, c] of border) grid[r][c] = color;
    return grid;
};
