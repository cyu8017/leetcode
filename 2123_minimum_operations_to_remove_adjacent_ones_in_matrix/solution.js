// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumOperations = function(grid) {
    const m = grid.length, n = grid[0].length;
    const id = Array.from({length: m}, () => new Array(n).fill(-1));
    let cnt = 0;
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] === 1) id[i][j] = cnt++;
    const g = Array.from({length: cnt}, () => []);
    const dirs = [[0,1],[1,0],[0,-1],[-1,0]];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] !== 1 || (i + j) % 2 !== 0) continue;
            const u = id[i][j];
            for (const [di, dj] of dirs) {
                const ni = i + di, nj = j + dj;
                if (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] === 1)
                    g[u].push(id[ni][nj]);
            }
        }
    }
    const match = new Array(cnt).fill(-1);
    const dfs = (u, seen) => {
        for (const v of g[u]) {
            if (seen[v]) continue;
            seen[v] = true;
            if (match[v] === -1 || dfs(match[v], seen)) {
                match[v] = u;
                return true;
            }
        }
        return false;
    };
    let ans = 0;
    for (let u = 0; u < cnt; u++) {
        let ok = false;
        for (let i = 0; i < m && !ok; i++)
            for (let j = 0; j < n; j++)
                if (id[i][j] === u && (i + j) % 2 === 0) { ok = true; break; }
        if (!ok) continue;
        const seen = new Array(cnt).fill(false);
        if (dfs(u, seen)) ans++;
    }
    return ans;
};
