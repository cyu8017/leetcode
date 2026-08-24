// LeetCode 3797 - Count Routes To Climb A Rectangular Grid
// https://leetcode.com/problems/count_routes_to_climb_a_rectangular_grid/

export function countRoutes(grid: any, d: any): any {
    const MOD = 1000000007;
    const n = grid.length, m = grid[0].length;
    let upRadius = 0;
    while ((upRadius + 1) * (upRadius + 1) + 1 <= d * d) upRadius++;
    let arrived = new Array(m).fill(0);
    for (let c = 0; c < m; c++) {
        if (grid[n - 1][c] === '.') arrived[c] = 1;
    }
    for (let r = n - 1; r >= 0; r--) {
        const pref = new Array(m + 1).fill(0);
        for (let i = 0; i < m; i++) pref[i + 1] = (pref[i] + arrived[i]) % MOD;
        const horizontal = new Array(m).fill(0);
        for (let c = 0; c < m; c++) {
            if (grid[r][c] === '#') continue;
            const l = Math.max(0, c - d), rr = Math.min(m - 1, c + d);
            horizontal[c] = (pref[rr + 1] - pref[l] - arrived[c]) % MOD;
            if (horizontal[c] < 0) horizontal[c] += MOD;
        }
        if (r === 0) {
            let ans = 0;
            for (let c = 0; c < m; c++) ans = (ans + arrived[c] + horizontal[c]) % MOD;
            return ans;
        }
        const pref2 = new Array(m + 1).fill(0);
        for (let c = 0; c < m; c++) pref2[c + 1] = (pref2[c] + arrived[c] + horizontal[c]) % MOD;
        const next = new Array(m).fill(0);
        for (let c = 0; c < m; c++) {
            if (grid[r - 1][c] === '#') continue;
            const l = Math.max(0, c - upRadius), rr = Math.min(m - 1, c + upRadius);
            next[c] = pref2[rr + 1] - pref2[l];
            if (next[c] < 0) next[c] += MOD;
        }
        arrived = next;
    }
    return 0;
}
