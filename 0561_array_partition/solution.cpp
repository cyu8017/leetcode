// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

#include <algorithm>
#include <vector>

class Solution {
public:
    int arrayPairSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int total = 0;
        for (std::size_t i = 0; i < nums.size(); i += 2) {
            total += nums[i];
        }
        return total;
    }
};
