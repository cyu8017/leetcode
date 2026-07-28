// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {
    const n = grid.length;
    if (grid[0][0] || grid[n - 1][n - 1]) return -1;
    const queue = [[0, 0, 1]];
    grid[0][0] = 1;
    let head = 0;
    while (head < queue.length) {
        const [r, c, dist] = queue[head++];
        if (r === n - 1 && c === n - 1) return dist;
        for (let dr = -1; dr <= 1; dr++) {
            for (let dc = -1; dc <= 1; dc++) {
                if (dr === 0 && dc === 0) continue;
                const nr = r + dr;
                const nc = c + dc;
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] === 0) {
                    grid[nr][nc] = 1;
                    queue.push([nr, nc, dist + 1]);
                }
            }
        }
    }
    return -1;
};
