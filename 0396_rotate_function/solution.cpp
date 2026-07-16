// LeetCode 0396 - Rotate Function
// https://leetcode.com/problems/rotate-function/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int maxRotateFunction(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        int current = 0;
        for (int index = 0; index < n; ++index) {
            current += index * nums[index];
        }

        int best = current;
        for (int index = n - 1; index > 0; --index) {
            current += total - n * nums[index];
            best = std::max(best, current);
        }

        return best;
    }
};
