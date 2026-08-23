// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var shortestPath = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    if (k >= m + n - 2) return m + n - 2;
    const queue = [[0, 0, k, 0]];
    const best = new Map([['0,0', k]]);
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    while (queue.length) {
        const [r, c, remaining, distance] = queue.shift();
        if (r === m - 1 && c === n - 1) return distance;
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            const nxt = remaining - grid[nr][nc];
            if (nxt < 0) continue;
            const key = `${nr},${nc}`;
            if (best.has(key) && nxt <= best.get(key)) continue;
            best.set(key, nxt);
            queue.push([nr, nc, nxt, distance + 1]);
        }
    }
    return -1;
};
