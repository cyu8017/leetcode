// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

#include <vector>

class Solution {
public:
    int minimumK(std::vector<int>& nums) {
        auto check = [&](int k) {
            long long t = 0;
            for (int x : nums) t += (x + k - 1) / k;
            return t <= 1LL * k * k;
        };
        int lo = 1, hi = 100000;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (check(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
