// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

export function numberOfRightTriangles(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const rows = new Array(m).fill(0), cols = new Array(n).fill(0);
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++) {
            rows[i] += grid[i][j];
            cols[j] += grid[i][j];
        }
    let ans = 0;
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] === 1)
                ans += (rows[i] - 1) * (cols[j] - 1);
    return ans;
}
