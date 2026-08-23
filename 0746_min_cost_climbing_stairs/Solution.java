// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int a = 0, b = 0;
        for (int i = cost.length - 1; i >= 0; i--) {
            int nextA = cost[i] + Math.min(a, b);
            b = a;
            a = nextA;
        }
        return Math.min(a, b);
    }
}
