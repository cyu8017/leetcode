// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxIncreasingGroups(std::vector<int>& usageLimits) {
        std::sort(usageLimits.begin(), usageLimits.end());
        int ans = 0;
        long long sum = 0;
        for (int v : usageLimits) {
            sum += v;
            long long need = 1LL * (ans + 1) * (ans + 2) / 2;
            if (sum >= need) ans++;
        }
        return ans;
    }
};
