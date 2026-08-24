// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

export function numMagicSquaresInside(grid: number[][]): number {
    const rows = grid.length, cols = grid[0].length;
    if (rows < 3 || cols < 3) return 0;
    const magic = (r, c) => {
        const vals = [];
        for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) vals.push(grid[r + i][c + j]);
        vals.sort((a, b) => a - b);
        for (let i = 0; i < 9; i++) if (vals[i] !== i + 1) return false;
        return grid[r][c] + grid[r][c + 1] + grid[r][c + 2] === 15
            && grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] === 15
            && grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] === 15
            && grid[r][c] + grid[r + 1][c] + grid[r + 2][c] === 15
            && grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] === 15
            && grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] === 15
            && grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] === 15
            && grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] === 15;
    };
    let ans = 0;
    for (let i = 0; i < rows - 2; i++) {
        for (let j = 0; j < cols - 2; j++) {
            if (magic(i, j)) ans++;
        }
    }
    return ans;
}
