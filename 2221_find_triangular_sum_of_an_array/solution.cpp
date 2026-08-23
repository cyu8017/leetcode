// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

#include <vector>

class Solution {
public:
    int triangularSum(std::vector<int>& nums) {
        while (nums.size() > 1) {
            std::vector<int> next(nums.size() - 1);
            for (size_t i = 0; i < next.size(); ++i) {
                next[i] = (nums[i] + nums[i + 1]) % 10;
            }
            nums = std::move(next);
        }
        return nums[0];
    }
};
