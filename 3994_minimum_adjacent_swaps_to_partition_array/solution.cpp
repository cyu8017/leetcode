// LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

#include <vector>

class Solution {
public:
    int minAdjacentSwaps(std::vector<int>& nums, int a, int b) {
        const int MOD = 1000000007;
        int result = 0, cnt1 = 0, cnt2 = 0;
        for (int x : nums) {
            if (x < a) {
                result = (result + cnt1 + cnt2) % MOD;
            } else if (x <= b) {
                ++cnt1;
                result = (result + cnt2) % MOD;
            } else {
                ++cnt2;
            }
        }
        return result;
    }
};
