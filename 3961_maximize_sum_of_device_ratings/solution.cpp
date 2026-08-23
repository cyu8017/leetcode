// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long maxRatings(std::vector<std::vector<int>>& units) {
        int n = (int)units[0].size();
        if (n == 1) {
            long long ans = 0;
            for (auto& x : units) ans += x[0];
            return ans;
        }
        long long ans = 0;
        int mn = INT_MAX, mn2 = INT_MAX;
        for (auto& x : units) {
            std::sort(x.begin(), x.end());
            ans += x[1];
            mn2 = std::min(mn2, x[1]);
            mn = std::min(mn, x[0]);
        }
        return ans - (mn2 - mn);
    }
};
