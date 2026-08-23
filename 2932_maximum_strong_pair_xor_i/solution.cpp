// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumStrongPairXor(std::vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++)
            for (int j = i; j < (int)nums.size(); j++) {
                int x = nums[i], y = nums[j];
                if (std::abs(x - y) <= std::min(x, y)) {
                    int xorr = x ^ y;
                    if (xorr > ans) ans = xorr;
                }
            }
        return ans;
    }
};
