// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumSafenessFactor = function(grid) {
    const n = grid.length;
    const dist = Array.from({length: n}, () => Array(n).fill(-1));
    const q = [];
    for (let i = 0; i < n; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] === 1) {
                dist[i][j] = 0;
                q.push([i, j]);
            }
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    for (let h = 0; h < q.length; h++) {
        const [x, y] = q[h];
        for (const [dx, dy] of dirs) {
            const ni = x + dx, nj = y + dy;
            if (ni >= 0 && nj >= 0 && ni < n && nj < n && dist[ni][nj] === -1) {
                dist[ni][nj] = dist[x][y] + 1;
                q.push([ni, nj]);
            }
        }
    }
    const ok = (sf) => {
        if (dist[0][0] < sf) return false;
        const seen = Array.from({length: n}, () => Array(n).fill(false));
        const st = [[0, 0]];
        seen[0][0] = true;
        while (st.length) {
            const [x, y] = st.pop();
            if (x === n - 1 && y === n - 1) return true;
            for (const [dx, dy] of dirs) {
                const ni = x + dx, nj = y + dy;
                if (ni >= 0 && nj >= 0 && ni < n && nj < n && !seen[ni][nj] && dist[ni][nj] >= sf) {
                    seen[ni][nj] = true;
                    st.push([ni, nj]);
                }
            }
        }
        return false;
    };
    let lo = 0, hi = n * n, ans = 0;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (ok(mid)) { ans = mid; lo = mid + 1; }
        else hi = mid - 1;
    }
    return ans;
};
