// LeetCode 1752 - Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

#include <vector>

class Solution {
public:
    bool check(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        int drops = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                drops++;
            }
        }
        return drops <= 1;
    }
};
