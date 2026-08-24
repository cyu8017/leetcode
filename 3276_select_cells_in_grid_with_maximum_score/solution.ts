// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

export function maxScore(grid: any): any {
    const m = grid.length;
    const vals = new Map();
    for (let i = 0; i < m; i++) {
        const seen = new Set();
        for (const v of grid[i]) {
            if (!seen.has(v)) {
                seen.add(v);
                if (!vals.has(v)) vals.set(v, []);
                vals.get(v).push(i);
            }
        }
    }
    const arr = [...vals.keys()].sort((a, b) => b - a);
    const N = 1 << m;
    let dp = new Array(N).fill(0);
    for (const v of arr) {
        const ndp = dp.slice();
        for (const r of vals.get(v)) {
            const bit = 1 << r;
            for (let mask = 0; mask < N; mask++) {
                if ((mask & bit) !== 0) continue;
                const cand = dp[mask] + v;
                const nmask = mask | bit;
                if (cand > ndp[nmask]) ndp[nmask] = cand;
            }
        }
        dp = ndp;
    }
    let ans = 0;
    for (const x of dp) ans = Math.max(ans, x);
    return ans;
}
