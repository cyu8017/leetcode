// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxFrequencyScore(std::vector<int>& nums, long long k) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        auto cost = [&](int l, int r) -> long long {
            int mid = (l + r) / 2;
            long long left = (long long)nums[mid] * (mid - l) - (pref[mid] - pref[l]);
            long long right = (pref[r + 1] - pref[mid + 1]) - (long long)nums[mid] * (r - mid);
            return left + right;
        };
        int ans = 1, left = 0;
        for (int right = 0; right < n; right++) {
            while (cost(left, right) > k) left++;
            ans = std::max(ans, right - left + 1);
        }
        return ans;
    }
};
