// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int x, int y) {
        auto ok = [&](int ops) {
            long long extra = 0;
            for (int v : nums) {
                long long remain = v - 1LL * ops * y;
                if (remain > 0) extra += (remain + (x - y) - 1) / (x - y);
            }
            return extra <= ops;
        };
        int lo = 0, hi = 0;
        for (int v : nums) {
            hi = std::max(hi, (v + y - 1) / y);
            hi = std::max(hi, (v + x - 1) / x);
        }
        hi += (int)nums.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
