// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    int waysToSplit(std::vector<int>& nums) {
        const long long mod = 1000000007LL;
        int n = static_cast<int>(nums.size());
        std::vector<long long> prefix(n);
        long long total = 0;
        for (int i = 0; i < n; i++) {
            total += nums[i];
            prefix[i] = total;
        }
        long long ans = 0;
        for (int i = 0; i < n - 2; i++) {
            long long left = prefix[i];
            auto first = prefix.begin() + i + 1;
            auto last = prefix.begin() + n - 1;
            auto lo = std::lower_bound(first, last, 2 * left);
            auto hi = std::upper_bound(lo, last, (total + left) / 2);
            ans = (ans + (hi - lo)) % mod;
        }
        return static_cast<int>(ans);
    }
};
