// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

#include <vector>

class Solution {
public:
    std::vector<int> minBitwiseArray(std::vector<int>& nums) {
        std::vector<int> ans(nums.size(), -1);
        for (int i = 0; i < (int)nums.size(); i++) {
            for (int x = 0; x < nums[i]; x++) {
                if ((x | (x + 1)) == nums[i]) { ans[i] = x; break; }
            }
        }
        return ans;
    }
};
