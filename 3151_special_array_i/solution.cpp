// LeetCode 3151 - Special Array I
// https://leetcode.com/problems/special-array-i/

#include <vector>

class Solution {
public:
    bool isArraySpecial(std::vector<int>& nums) {
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i] % 2 == nums[i - 1] % 2) return false;
        }
        return true;
    }
};
