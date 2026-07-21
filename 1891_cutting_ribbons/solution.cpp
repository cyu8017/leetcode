// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxLength(std::vector<int>& ribbons, int k) {
        auto can = [&](int length) {
            long long total = 0;
            for (int ribbon : ribbons) {
                total += ribbon / length;
            }
            return total >= k;
        };

        int lo = 1;
        int hi = *std::max_element(ribbons.begin(), ribbons.end());
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (can(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return can(lo) ? lo : 0;
    }
};
