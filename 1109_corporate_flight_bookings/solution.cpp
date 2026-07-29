// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

#include <vector>

class Solution {
public:
    std::vector<int> corpFlightBookings(std::vector<std::vector<int>>& bookings, int n) {
        std::vector<int> diff(n + 1, 0);
        for (const auto& b : bookings) {
            diff[b[0] - 1] += b[2];
            diff[b[1]] -= b[2];
        }
        std::vector<int> ans(n);
        int cur = 0;
        for (int i = 0; i < n; ++i) {
            cur += diff[i];
            ans[i] = cur;
        }
        return ans;
    }
};
