// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int maximumWealth(std::vector<std::vector<int>>& accounts) {
        int best = 0;
        for (const auto& row : accounts) {
            best = std::max(best, std::accumulate(row.begin(), row.end(), 0));
        }
        return best;
    }
};
