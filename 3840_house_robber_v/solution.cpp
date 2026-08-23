// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long rob(std::vector<int>& nums, std::vector<int>& colors) {
        int n = (int)nums.size();
        int64_t f = 0, g = nums[0];
        for (int i = 1; i < n; i++) {
            if (colors[i - 1] == colors[i]) {
                int64_t nf = std::max(f, g);
                g = f + nums[i];
                f = nf;
            } else {
                int64_t nf = std::max(f, g);
                g = nf + nums[i];
                f = nf;
            }
        }
        return std::max(f, g);
    }
};
