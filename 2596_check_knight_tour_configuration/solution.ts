// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

export function checkValidGrid(grid: number[][]): boolean {
    const n = grid.length;
    if (grid[0][0] !== 0) return false;
    const pos = new Array(n * n);
    for (let i = 0; i < n; ++i)
        for (let j = 0; j < n; ++j)
            pos[grid[i][j]] = [i, j];
    const dirs = [
        [1, 2], [1, -2], [-1, 2], [-1, -2],
        [2, 1], [2, -1], [-2, 1], [-2, -1],
    ];
    for (let v = 0; v + 1 < n * n; ++v) {
        const r = pos[v][0], c = pos[v][1];
        let ok = false;
        for (const d of dirs) {
            if (r + d[0] === pos[v + 1][0] && c + d[1] === pos[v + 1][1]) {
                ok = true;
                break;
            }
        }
        if (!ok) return false;
    }
    return true;
}
