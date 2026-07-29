// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minCostClimbingStairs(std::vector<int>& cost) {
        int a = 0;
        int b = 0;
        for (int i = static_cast<int>(cost.size()) - 1; i >= 0; --i) {
            int nextA = cost[i] + std::min(a, b);
            b = a;
            a = nextA;
        }
        return std::min(a, b);
    }
};
