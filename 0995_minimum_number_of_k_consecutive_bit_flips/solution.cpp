// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

#include <vector>

class Solution {
public:
    int minKBitFlips(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> flip(n, 0);
        int ans = 0, flipped = 0;
        for (int i = 0; i < n; i++) {
            if (i >= k) flipped ^= flip[i - k];
            if (nums[i] == flipped) {
                if (i + k > n) return -1;
                ans++;
                flipped ^= 1;
                flip[i] = 1;
            }
        }
        return ans;
    }
};
