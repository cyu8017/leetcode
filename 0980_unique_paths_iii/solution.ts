// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

export function uniquePathsIII(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    let empty = 0, sr = 0, sc = 0, ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] !== -1) empty++;
            if (grid[i][j] === 1) { sr = i; sc = j; }
        }
    }
    const dfs = (r, c, remain) => {
        if (grid[r][c] === 2) {
            if (remain === 1) ans++;
            return;
        }
        const temp = grid[r][c];
        grid[r][c] = -1;
        const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] !== -1)
                dfs(nr, nc, remain - 1);
        }
        grid[r][c] = temp;
    };
    dfs(sr, sc, empty);
    return ans;
}
