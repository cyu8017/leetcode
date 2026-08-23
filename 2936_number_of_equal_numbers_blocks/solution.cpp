// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

#include <vector>

class Solution {
public:
    int blockCount(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        int ans = 1;
        for (int i = 1; i < (int)nums.size(); i++)
            if (nums[i] != nums[i - 1]) ans++;
        return ans;
    }
};
