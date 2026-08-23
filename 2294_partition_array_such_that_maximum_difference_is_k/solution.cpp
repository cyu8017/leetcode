// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

#include <vector>
#include <algorithm>

class Solution {
public:
    int partitionArray(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int ans = 1, start = nums[0];
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] - start > k) { ans++; start = nums[i]; }
        }
        return ans;
    }
};
