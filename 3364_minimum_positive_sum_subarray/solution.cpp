// LeetCode 3364 - Minimum Positive Sum Subarray 
// https://leetcode.com/problems/minimum-positive-sum-subarray/

#include <climits>
#include <vector>

class Solution {
public:
    int minimumSumSubarray(std::vector<int>& nums, int l, int r) {
        int n = (int)nums.size();
        std::vector<int> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        int ans = INT_MAX;
        bool found = false;
        for (int i = 0; i < n; i++) {
            for (int length = l; length <= r && i + length <= n; length++) {
                int s = pref[i + length] - pref[i];
                if (s > 0 && s < ans) {
                    ans = s;
                    found = true;
                }
            }
        }
        return found ? ans : -1;
    }
};
