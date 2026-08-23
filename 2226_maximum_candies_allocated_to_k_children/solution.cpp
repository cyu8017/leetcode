// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumCandies(std::vector<int>& candies, long long k) {
        int mx = 0;
        for (int c : candies) mx = std::max(mx, c);
        int lo = 0, hi = mx;
        auto can = [&](int mid) {
            if (mid == 0) return true;
            long long cnt = 0;
            for (int c : candies) {
                cnt += c / mid;
                if (cnt >= k) return true;
            }
            return false;
        };
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
