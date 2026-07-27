// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

#include <vector>

class Solution {
public:
    std::vector<bool> prefixesDivBy5(std::vector<int>& nums) {
        std::vector<bool> ans;
        ans.reserve(nums.size());
        int rem = 0;
        for (int bit : nums) {
            rem = (rem * 2 + bit) % 5;
            ans.push_back(rem == 0);
        }
        return ans;
    }
};

