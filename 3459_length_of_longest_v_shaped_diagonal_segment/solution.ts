// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

export function lenOfVDiagonal(grid: any): any {
    const m = grid.length, n = grid[0].length;
    const dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]];
    const nextDir = [1, 2, 3, 0];
    const memo = new Map();
    const key = (i, j, d, turned, expect) =>
        ((((i * 101 + j) * 5 + d) * 3 + turned) * 5 + expect);
    const dfs = (i, j, d, turned, expect) => {
        if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] !== expect) return 0;
        const k = key(i, j, d, turned, expect);
        if (memo.has(k)) return memo.get(k);
        const ni = i + dirs[d][0], nj = j + dirs[d][1];
        const nx = expect === 2 ? 0 : 2;
        let best = 1 + dfs(ni, nj, d, turned, nx);
        if (turned === 0) {
            const nd = nextDir[d];
            const ti = i + dirs[nd][0], tj = j + dirs[nd][1];
            const cand = 1 + dfs(ti, tj, nd, 1, nx);
            if (cand > best) best = cand;
        }
        memo.set(k, best);
        return best;
    };
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] !== 1) continue;
            for (let d = 0; d < 4; d++) {
                const ni = i + dirs[d][0], nj = j + dirs[d][1];
                const best = 1 + dfs(ni, nj, d, 0, 2);
                if (best > ans) ans = best;
            }
            if (ans < 1) ans = 1;
        }
    }
    return ans;
}
