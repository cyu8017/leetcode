// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

export function minCuttingCost(n: any, m: any, k: any): any {
    const x = Math.max(n, m);
    if (x <= k) return 0;
    return k * (x - k);
}
