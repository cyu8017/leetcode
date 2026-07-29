// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

#include <vector>

class Solution {
public:
    std::vector<int> sortArrayByParity(std::vector<int>& nums) {
        int i = 0;
        for (int j = 0; j < (int)nums.size(); j++) {
            if (nums[j] % 2 == 0) {
                std::swap(nums[i], nums[j]);
                i++;
            }
        }
        return nums;
    }
};
