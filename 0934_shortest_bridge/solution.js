// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestBridge = function(grid) {
    const n = grid.length;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const q = [];
    const dfs = (i, j) => {
        if (i < 0 || j < 0 || i >= n || j >= n || grid[i][j] !== 1) return;
        grid[i][j] = 2;
        q.push([i, j]);
        for (const [di, dj] of dirs) dfs(i + di, j + dj);
    };
    let found = false;
    for (let i = 0; i < n && !found; i++) {
        for (let j = 0; j < n && !found; j++) {
            if (grid[i][j] === 1) {
                dfs(i, j);
                found = true;
            }
        }
    }
    let steps = 0;
    while (q.length) {
        const sz = q.length;
        for (let s = 0; s < sz; s++) {
            const [i, j] = q.shift();
            for (const [di, dj] of dirs) {
                const ni = i + di, nj = j + dj;
                if (ni < 0 || nj < 0 || ni >= n || nj >= n) continue;
                if (grid[ni][nj] === 1) return steps;
                if (grid[ni][nj] === 0) {
                    grid[ni][nj] = 2;
                    q.push([ni, nj]);
                }
            }
        }
        steps++;
    }
    return -1;
};
