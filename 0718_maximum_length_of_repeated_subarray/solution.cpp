// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findLength(std::vector<int>& nums1, std::vector<int>& nums2) {
        int m = static_cast<int>(nums1.size());
        int n = static_cast<int>(nums2.size());
        std::vector<int> dp(n + 1, 0);
        int best = 0;
        for (int i = 1; i <= m; ++i) {
            std::vector<int> next(n + 1, 0);
            for (int j = 1; j <= n; ++j) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    next[j] = dp[j - 1] + 1;
                    best = std::max(best, next[j]);
                }
            }
            dp.swap(next);
        }
        return best;
    }
};
