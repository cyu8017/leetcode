// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

#include <cstdlib>
#include <vector>

class Solution {
public:
    bool isIdealPermutation(std::vector<int>& nums) {
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (std::abs(nums[i] - i) > 1) {
                return false;
            }
        }
        return true;
    }
};
