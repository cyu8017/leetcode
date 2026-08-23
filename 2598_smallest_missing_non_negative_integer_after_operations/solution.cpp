// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

#include <vector>

class Solution {
public:
    int findSmallestInteger(std::vector<int>& nums, int value) {
        std::vector<int> cnt(value);
        for (int x : nums) {
            int r = x % value;
            if (r < 0) r += value;
            cnt[r]++;
        }
        int mex = 0;
        while (cnt[mex % value] > 0) {
            cnt[mex % value]--;
            mex++;
        }
        return mex;
    }
};
