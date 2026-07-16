// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

#include <vector>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        if (nums.size() <= 2) {
            return static_cast<int>(nums.size());
        }

        int write = 2;
        for (int i = 2; i < static_cast<int>(nums.size()); i++) {
            if (nums[i] != nums[write - 2]) {
                nums[write] = nums[i];
                write++;
            }
        }

        return write;
    }
};
