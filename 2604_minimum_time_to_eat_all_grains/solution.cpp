// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumTime(std::vector<int>& hens, std::vector<int>& grains) {
        std::sort(hens.begin(), hens.end());
        std::sort(grains.begin(), grains.end());
        auto ok = [&](int t) {
            int j = 0;
            for (int h : hens) {
                if (j >= (int)grains.size()) return true;
                if (grains[j] >= h) {
                    while (j < (int)grains.size() && grains[j] - h <= t) j++;
                } else {
                    if (h - grains[j] > t) return false;
                    int left = h - grains[j];
                    int maxRight1 = t - 2 * left;
                    int maxRight2 = (t - left) / 2;
                    int reach = h;
                    if (maxRight1 > maxRight2) {
                        if (maxRight1 > 0) reach = h + maxRight1;
                    } else {
                        if (maxRight2 > 0) reach = h + maxRight2;
                    }
                    while (j < (int)grains.size() && grains[j] <= reach) j++;
                }
            }
            return j >= (int)grains.size();
        };
        int lo = 0, hi = (int)2e9;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
