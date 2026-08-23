// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums1, std::vector<int>& nums2) {
        long long ans = 1;
        int n = (int)nums1.size();
        bool ok = false;
        int d = 1 << 30;
        for (int i = 0; i < n; i++) {
            int x = std::max(nums1[i], nums2[i]);
            int y = std::min(nums1[i], nums2[i]);
            ans += x - y;
            d = std::min(d, std::min(std::abs(x - nums2[n]), std::abs(y - nums2[n])));
            if (nums2[n] >= y && nums2[n] <= x) ok = true;
        }
        if (!ok) ans += d;
        return ans;
    }
};
