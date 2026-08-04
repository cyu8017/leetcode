// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var containsCycle = function(grid) {
    const m = grid.length, n = grid[0].length;
    const seen = Array.from({ length: m }, () => Array(n).fill(false));
    const dfs = (r, c, pr, pc) => {
        seen[r][c] = true;
        for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] !== grid[r][c] || (nr === pr && nc === pc)) continue;
            if (seen[nr][nc] || dfs(nr, nc, r, c)) return true;
        }
        return false;
    };
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (!seen[r][c] && dfs(r, c, -1, -1)) return true;
        }
    }
    return false;
};
