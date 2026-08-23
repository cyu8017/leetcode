// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::vector<std::vector<int>> snail(std::vector<int>& nums, int rowsCount, int colsCount) {
        if (rowsCount * colsCount != (int)nums.size()) return {};
        std::vector<std::vector<int>> ans(rowsCount, std::vector<int>(colsCount));
        int idx = 0;
        for (int c = 0; c < colsCount; ++c) {
            if (c % 2 == 0) {
                for (int r = 0; r < rowsCount; ++r) ans[r][c] = nums[idx++];
            } else {
                for (int r = rowsCount - 1; r >= 0; --r) ans[r][c] = nums[idx++];
            }
        }
        return ans;
    }
};
