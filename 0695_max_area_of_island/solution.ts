// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

export function maxAreaOfIsland(grid: number[][]): number {
    const dfs = (r, c) => {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] === 0) return 0;
        grid[r][c] = 0;
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1);
    };
    let best = 0;
    for (let i = 0; i < grid.length; i++)
        for (let j = 0; j < grid[0].length; j++)
            best = Math.max(best, dfs(i, j));
    return best;
}
