// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var largestIsland = function(grid) {
    const n = grid.length;
    const sizes = new Map([[0, 0]]);
    let islandId = 2;
    const dfs = (r, c, iid) => {
        if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] !== 1) return 0;
        grid[r][c] = iid;
        return 1 + dfs(r + 1, c, iid) + dfs(r - 1, c, iid) + dfs(r, c + 1, iid) + dfs(r, c - 1, iid);
    };
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                sizes.set(islandId, dfs(i, j, islandId));
                islandId++;
            }
        }
    }
    let ans = 0;
    for (const v of sizes.values()) ans = Math.max(ans, v);
    const dr = [1, -1, 0, 0], dc = [0, 0, 1, -1];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] !== 0) continue;
            const seen = new Set();
            let total = 1;
            for (let k = 0; k < 4; k++) {
                const ni = i + dr[k], nj = j + dc[k];
                if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                    const iid = grid[ni][nj];
                    if (iid > 1 && !seen.has(iid)) {
                        seen.add(iid);
                        total += sizes.get(iid);
                    }
                }
            }
            ans = Math.max(ans, total);
        }
    }
    return ans;
};
