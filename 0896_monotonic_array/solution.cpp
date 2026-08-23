// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

#include <vector>

class Solution {
public:
    bool isMonotonic(std::vector<int>& nums) {
        bool inc = true, dec = true;
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] < nums[i - 1]) {
                inc = false;
            }
            if (nums[i] > nums[i - 1]) {
                dec = false;
            }
        }
        return inc || dec;
    }
};
