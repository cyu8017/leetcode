// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumStrongPairXor(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            int x = nums[i];
            for (int j = i; j < (int)nums.size() && nums[j] <= 2 * x; j++) {
                int xorr = x ^ nums[j];
                if (xorr > ans) ans = xorr;
            }
        }
        return ans;
    }
};
