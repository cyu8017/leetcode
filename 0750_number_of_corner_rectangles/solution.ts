// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

export function countCornerRectangles(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = i + 1; j < m; j++) {
            let count = 0;
            for (let c = 0; c < n; c++) if (grid[i][c] === 1 && grid[j][c] === 1) count++;
            ans += count * (count - 1) / 2;
        }
    }
    return ans;
}
