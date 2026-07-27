// LeetCode 1005 - Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int largestSumAfterKNegations(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < static_cast<int>(nums.size()) && k > 0; ++i) {
            if (nums[i] < 0) {
                nums[i] = -nums[i];
                --k;
            }
        }
        if (k % 2) {
            std::sort(nums.begin(), nums.end());
            nums[0] = -nums[0];
        }
        return std::accumulate(nums.begin(), nums.end(), 0);
    }
};

