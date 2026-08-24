// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

export function minimumCost(nums: any, cost: any, k: any): any {
    const n = nums.length;
    const pn = new Array(n + 1).fill(0), pc = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        pn[i + 1] = pn[i] + nums[i];
        pc[i + 1] = pc[i] + cost[i];
    }
    const inf = Number.MAX_SAFE_INTEGER / 4;
    const dp = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) dp[i] = inf;
    for (let i = n - 1; i >= 0; i--) {
        for (let j = i; j < n; j++) {
            const cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k * (pc[n] - pc[i]) + dp[j + 1];
            if (cand < dp[i]) dp[i] = cand;
        }
    }
    return dp[0];
}
