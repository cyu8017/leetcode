// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    let a = 0, b = 0;
    for (let i = cost.length - 1; i >= 0; i--) {
        const nextA = cost[i] + Math.min(a, b);
        b = a;
        a = nextA;
    }
    return Math.min(a, b);
};
