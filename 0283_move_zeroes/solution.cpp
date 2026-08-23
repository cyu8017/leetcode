// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

#include <vector>

class Solution {
public:
    void moveZeroes(std::vector<int>& nums) {
        int insert = 0;
        for (int num : nums) {
            if (num != 0) {
                nums[insert++] = num;
            }
        }
        for (int index = insert; index < static_cast<int>(nums.size()); index++) {
            nums[index] = 0;
        }
    }
};
