// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

export function minCost(n: any, cost: any): any {
    const inf = Number.MAX_SAFE_INTEGER / 4;
    const m = Math.floor(n / 2);
    let dp = Array.from({ length: 3 }, () => new Array(3).fill(0));
    for (let a = 0; a < 3; a++) {
        for (let b = 0; b < 3; b++) {
            dp[a][b] = (a === b) ? inf : cost[0][a] + cost[n - 1][b];
        }
    }
    for (let i = 1; i < m; i++) {
        const ndp = Array.from({ length: 3 }, () => new Array(3).fill(inf));
        for (let pa = 0; pa < 3; pa++) {
            for (let pb = 0; pb < 3; pb++) {
                if (dp[pa][pb] >= inf) continue;
                for (let a = 0; a < 3; a++) {
                    if (a === pa) continue;
                    for (let b = 0; b < 3; b++) {
                        if (b === pb || a === b) continue;
                        const v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b];
                        if (v < ndp[a][b]) ndp[a][b] = v;
                    }
                }
            }
        }
        dp = ndp;
    }
    let ans = inf;
    for (let a = 0; a < 3; a++) for (let b = 0; b < 3; b++) if (dp[a][b] < ans) ans = dp[a][b];
    return ans;
}
