// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

#include <vector>

class Solution {
public:
    std::vector<int> minBitwiseArray(std::vector<int>& nums) {
        std::vector<int> ans(nums.size(), -1);
        for (int i = 0; i < (int)nums.size(); i++) {
            int n = nums[i];
            if (n == 2) continue;
            for (int b = 0; b < 31; b++) {
                if (((n >> b) & 1) == 0) continue;
                int x = n ^ (1 << b);
                if ((x | (x + 1)) == n) { ans[i] = x; break; }
            }
        }
        return ans;
    }
};
