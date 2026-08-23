// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

#include <vector>

class Solution {
public:
    bool canSplitArray(std::vector<int>& nums, int m) {
        int n = (int)nums.size();
        if (n <= 2) return true;
        for (int i = 0; i + 1 < n; i++) {
            if (nums[i] + nums[i + 1] >= m) return true;
        }
        return false;
    }
};
