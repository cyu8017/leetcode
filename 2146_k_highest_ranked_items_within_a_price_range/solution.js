// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

/**
 * @param {number[][]} grid
 * @param {number[]} pricing
 * @param {number[]} start
 * @param {number} k
 * @return {number[][]}
 */
var highestRankedKItems = function(grid, pricing, start, k) {
    const m = grid.length, n = grid[0].length;
    const low = pricing[0], high = pricing[1];
    const vis = Array.from({length: m}, () => new Array(n).fill(false));
    const q = [[start[0], start[1], 0]];
    vis[start[0]][start[1]] = true;
    const cands = [];
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    while (q.length) {
        const [r, c, d] = q.shift();
        if (grid[r][c] >= low && grid[r][c] <= high)
            cands.push([d, grid[r][c], r, c]);
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] && grid[nr][nc] !== 0) {
                vis[nr][nc] = true;
                q.push([nr, nc, d + 1]);
            }
        }
    }
    cands.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2] || a[3] - b[3]);
    if (k > cands.length) k = cands.length;
    const ans = [];
    for (let i = 0; i < k; i++) ans.push([cands[i][2], cands[i][3]]);
    return ans;
};
