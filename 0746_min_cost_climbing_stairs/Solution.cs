// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

using System;

public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        int a = 0, b = 0;
        for (int i = cost.Length - 1; i >= 0; i--) {
            int nextA = cost[i] + Math.Min(a, b);
            b = a;
            a = nextA;
        }
        return Math.Min(a, b);
    }
}
