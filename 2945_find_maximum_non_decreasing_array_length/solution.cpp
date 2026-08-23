// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

#include <vector>

class Solution {
public:
    int findMaximumLength(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1), last(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        std::vector<int> dp(n + 1);
        std::vector<std::pair<int, long long>> dq = {{0, 0}};
        for (int i = 1; i <= n; i++) {
            while (dq.size() > 1 && dq[1].second <= pref[i]) dq.erase(dq.begin());
            int j = dq[0].first;
            dp[i] = dp[j] + 1;
            last[i] = pref[i] - pref[j];
            long long val = pref[i] + last[i];
            while (!dq.empty() && dq.back().second >= val) dq.pop_back();
            dq.push_back({i, val});
        }
        return dp[n];
    }
};
