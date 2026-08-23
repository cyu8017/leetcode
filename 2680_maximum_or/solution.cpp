// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

#include <vector>

class Solution {
public:
    long long maximumOr(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1), suf(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] | nums[i];
        for (int i = n - 1; i >= 0; i--) suf[i] = suf[i + 1] | nums[i];
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long cur = pref[i] | ((long long)nums[i] << k) | suf[i + 1];
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};
