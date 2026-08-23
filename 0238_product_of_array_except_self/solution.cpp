// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int length = static_cast<int>(nums.size());
        std::vector<int> result(length, 1);
        int prefix = 1;
        for (int index = 0; index < length; index++) {
            result[index] = prefix;
            prefix *= nums[index];
        }
        int suffix = 1;
        for (int index = length - 1; index >= 0; index--) {
            result[index] *= suffix;
            suffix *= nums[index];
        }
        return result;
    }
};
