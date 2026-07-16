// LeetCode 0200 - Number of Islands
// https://leetcode.com/problems/number-of-islands/

export function numIslands(grid: string[][]): number {
    if (grid.length === 0) {
        return 0;
    }

    const rows = grid.length;
    const cols = grid[0].length;
    let count = 0;

    const dfs = (row: number, col: number): void => {
        if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] !== "1") {
            return;
        }
        grid[row][col] = "0";
        dfs(row + 1, col);
        dfs(row - 1, col);
        dfs(row, col + 1);
        dfs(row, col - 1);
    };

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (grid[row][col] === "1") {
                count++;
                dfs(row, col);
            }
        }
    }
    return count;
}