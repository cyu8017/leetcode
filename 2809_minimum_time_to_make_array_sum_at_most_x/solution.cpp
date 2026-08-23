// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumTime(std::vector<int>& nums1, std::vector<int>& nums2, int x) {
        int n = (int)nums1.size();
        std::vector<std::pair<int, int>> arr(n);
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = {nums1[i], nums2[i]};
            sum1 += nums1[i];
            sum2 += nums2[i];
        }
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.second < b.second; });
        std::vector<int> dp(n + 1, 0);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j >= 1; j--) {
                dp[j] = std::max(dp[j], dp[j - 1] + arr[i].first + j * arr[i].second);
            }
        }
        for (int t = 0; t <= n; t++) {
            if (sum1 + sum2 * t - dp[t] <= x) return t;
        }
        return -1;
    }
};
