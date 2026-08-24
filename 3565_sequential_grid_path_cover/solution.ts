// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

export function findPath(grid: any, k: any): any {
    const m = grid.length, n = grid[0].length;
    const dirs = [-1, 0, 1, 0, -1];
    let st = 0n;
    const path = [];
    function f(i: any, j: any): any { return i * n + j; }    function dfs(i: any, j: any, v: any): any {
        path.push([i, j]);
        if (path.length === m * n) return true;
        const idx = f(i, j);
        st |= 1n << BigInt(idx);
        if (grid[i][j] === v) v++;
        for (let t = 0; t < 4; t++) {
            const x = i + dirs[t], y = j + dirs[t + 1];
            if (0 <= x && x < m && 0 <= y && y < n) {
                const idx2 = f(x, y);
                if (((st >> BigInt(idx2)) & 1n) === 0n && (grid[x][y] === 0 || grid[x][y] === v)) {
                    if (dfs(x, y, v)) return true;
                }
            }
        }
        path.pop();
        st ^= 1n << BigInt(idx);
        return false;
    }    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 0 || grid[i][j] === 1) {
                if (dfs(i, j, 1)) return path;
                path.length = 0;
                st = 0n;
            }
        }
    }
    return [];
}
