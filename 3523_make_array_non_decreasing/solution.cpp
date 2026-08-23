// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

#include <vector>

class Solution {
public:
    int maximumPossibleSize(std::vector<int>& nums) {
        int ans = 0, mx = 0;
        for (int x : nums) {
            if (mx <= x) {
                ans++;
                mx = x;
            }
        }
        return ans;
    }
};
