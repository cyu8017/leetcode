// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        int xorr = 0;
        for (int v : nums) xorr ^= v;
        int diff = xorr ^ k;
        int ans = 0;
        while (diff > 0) {
            ans += diff & 1;
            diff >>= 1;
        }
        return ans;
    }
};
