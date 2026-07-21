// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

#include <vector>

class Solution {
public:
    std::vector<int> getMaximumXor(std::vector<int>& nums, int maximumBit) {
        int limit = (1 << maximumBit) - 1;
        int current = 0;
        for (int num : nums) {
            current ^= num;
        }
        std::vector<int> result;
        result.reserve(nums.size());
        for (int i = static_cast<int>(nums.size()) - 1; i >= 0; --i) {
            result.push_back(current ^ limit);
            current ^= nums[i];
        }
        return result;
    }
};
