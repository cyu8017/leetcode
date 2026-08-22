// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

int minCostClimbingStairs(int* cost, int costSize) {
    int a = 0, b = 0;
    for (int i = costSize - 1; i >= 0; i--) {
        int na = cost[i] + (a < b ? a : b);
        b = a;
        a = na;
    }
    return a < b ? a : b;
}
