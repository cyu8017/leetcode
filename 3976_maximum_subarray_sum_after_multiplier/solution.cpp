// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

#include <algorithm>
#include <array>
#include <climits>
#include <vector>

class Solution {
public:
    long long maxSubarraySum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        const long long inf = LLONG_MIN / 4;
        std::vector<std::array<long long, 4>> f(n + 1);
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < 4; j++) f[i][j] = inf;
        }
        f[0][0] = 0;
        long long ans = inf;
        for (int i = 1; i <= n; i++) {
            long long x = nums[i - 1];
            f[i][0] = std::max(f[i - 1][0], 0LL) + x;
            f[i][1] = std::max({f[i - 1][0], f[i - 1][1], 0LL}) + x * k;
            f[i][2] = std::max({f[i - 1][0], f[i - 1][2], 0LL}) + x / k;
            f[i][3] = std::max({f[i - 1][1], f[i - 1][2], f[i - 1][3]}) + x;
            ans = std::max({ans, f[i][0], f[i][1], f[i][2], f[i][3]});
        }
        return ans;
    }
};
