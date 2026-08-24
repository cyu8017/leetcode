// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

export function gridGame(grid: number[][]): number {
    const n = grid[0].length;
    let top = 0, bottom = 0, ans = Number.MAX_SAFE_INTEGER;
    for (const v of grid[0]) top += v;
    for (let i = 0; i < n; i++) {
        top -= grid[0][i];
        ans = Math.min(ans, Math.max(top, bottom));
        bottom += grid[1][i];
    }
    return ans;
}
