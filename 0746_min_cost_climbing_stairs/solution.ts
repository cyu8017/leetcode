// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

export function minCostClimbingStairs(cost: number[]): number {
    let a = 0, b = 0;
    for (let i = cost.length - 1; i >= 0; i--) {
        const nextA = cost[i] + Math.min(a, b);
        b = a;
        a = nextA;
    }
    return Math.min(a, b);
}
