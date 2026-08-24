// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

export function satisfiesConditions(grid: number[][]): boolean {
    const m = grid.length, n = grid[0].length;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const x = grid[i][j];
            if (i + 1 < m && x !== grid[i + 1][j]) return false;
            if (j + 1 < n && x === grid[i][j + 1]) return false;
        }
    }
    return true;
}
