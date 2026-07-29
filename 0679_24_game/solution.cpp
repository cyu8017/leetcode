// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

#include <cmath>
#include <vector>

class Solution {
    static constexpr double eps = 1e-6;

    bool dfs(std::vector<double> nums) {
        if (nums.size() == 1) {
            return std::fabs(nums[0] - 24.0) < eps;
        }
        for (std::size_t i = 0; i < nums.size(); ++i) {
            for (std::size_t j = 0; j < nums.size(); ++j) {
                if (i == j) {
                    continue;
                }
                std::vector<double> rest;
                for (std::size_t k = 0; k < nums.size(); ++k) {
                    if (k != i && k != j) {
                        rest.push_back(nums[k]);
                    }
                }
                const double a = nums[i];
                const double b = nums[j];
                std::vector<double> candidates = {a + b, a - b, a * b};
                if (std::fabs(b) > eps) {
                    candidates.push_back(a / b);
                }
                for (double value : candidates) {
                    rest.push_back(value);
                    if (dfs(rest)) {
                        return true;
                    }
                    rest.pop_back();
                }
            }
        }
        return false;
    }

public:
    bool judgePoint24(std::vector<int>& cards) {
        std::vector<double> nums;
        for (int card : cards) {
            nums.push_back(static_cast<double>(card));
        }
        return dfs(nums);
    }
};
