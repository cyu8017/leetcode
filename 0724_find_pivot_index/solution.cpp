// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

#include <numeric>
#include <vector>

class Solution {
public:
    int pivotIndex(std::vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        int left = 0;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (left == total - left - nums[i]) {
                return i;
            }
            left += nums[i];
        }
        return -1;
    }
};
