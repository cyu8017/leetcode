// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

function tryCand(ndp: any, base: any, na: any, nb: any, v: any): any {
    if (base + v < ndp[na][nb]) ndp[na][nb] = base + v;
}export function minArraySum(nums: any, k: any, op1: any, op2: any): any {
    const inf = 1e18;
    let dp = Array.from({length: op1 + 1}, () => new Array(op2 + 1).fill(inf));
    dp[0][0] = 0;
    for (const x of nums) {
        const ndp = Array.from({length: op1 + 1}, () => new Array(op2 + 1).fill(inf));
        for (let a = 0; a <= op1; a++) {
            for (let b = 0; b <= op2; b++) {
                if (dp[a][b] === inf) continue;
                tryCand(ndp, dp[a][b], a, b, x);
                if (a < op1) tryCand(ndp, dp[a][b], a + 1, b, Math.floor((x + 1) / 2));
                if (b < op2 && x >= k) tryCand(ndp, dp[a][b], a, b + 1, x - k);
                if (a < op1 && b < op2) {
                    const v1 = Math.floor((x + 1) / 2);
                    if (v1 >= k) tryCand(ndp, dp[a][b], a + 1, b + 1, v1 - k);
                    if (x >= k) tryCand(ndp, dp[a][b], a + 1, b + 1, Math.floor((x - k + 1) / 2));
                }
            }
        }
        dp = ndp;
    }
    let ans = inf;
    for (let a = 0; a <= op1; a++)
        for (let b = 0; b <= op2; b++)
            if (dp[a][b] < ans) ans = dp[a][b];
    return ans;
}
