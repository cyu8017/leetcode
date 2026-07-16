// LeetCode 0027 - Remove Element
// https://leetcode.com/problems/remove-element/

#include <vector>

class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        int write = 0;
        for (int read = 0; read < static_cast<int>(nums.size()); read++) {
            if (nums[read] != val) {
                nums[write] = nums[read];
                write++;
            }
        }
        return write;
    }
};
