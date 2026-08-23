// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/

#include <algorithm>
#include <cstdint>
#include <numeric>
#include <vector>

class Solution {
public:
    long long maxPairStrength(std::vector<int>& nums) {
        int n = (int)nums.size();
        int64_t ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int64_t g = std::gcd((int64_t)nums[i], (int64_t)nums[j]);
                int64_t x = (int64_t)nums[i] * (int64_t)nums[j] / (g * g);
                ans = std::max(ans, x);
            }
        }
        return ans;
    }
};
