// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

#include <vector>

class Solution {
    int pop(int x) {
        int c = 0;
        while (x) { c += x & 1; x >>= 1; }
        return c;
    }
public:
    int maxProfit(int n, std::vector<std::vector<int>>& edges, std::vector<int>& score) {
        std::vector<int> need(n), dp(1 << n, -1);
        dp[0] = 0;
        for (auto& e : edges) need[e[1]] |= 1 << e[0];
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] < 0) continue;
            int pos = pop(mask) + 1;
            for (int i = 0; i < n; i++) {
                if ((mask >> i) & 1) continue;
                if ((mask & need[i]) == need[i]) {
                    int nm = mask | (1 << i);
                    int v = dp[mask] + score[i] * pos;
                    if (v > dp[nm]) dp[nm] = v;
                }
            }
        }
        return dp[(1 << n) - 1];
    }
};
