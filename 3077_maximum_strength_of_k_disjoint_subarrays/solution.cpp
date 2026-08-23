// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long maximumStrength(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        const long long inf = LLONG_MIN / 2;
        std::vector<std::vector<std::vector<long long>>> f(n + 1,
            std::vector<std::vector<long long>>(k + 1, std::vector<long long>(2, inf)));
        f[0][0][0] = 0;
        for (int i = 1; i <= n; i++) {
            long long x = nums[i - 1];
            for (int j = 0; j <= k; j++) {
                long long sign = (j & 1) ? 1 : -1;
                long long val = sign * x * (k - j + 1);
                f[i][j][0] = std::max(f[i - 1][j][0], f[i - 1][j][1]);
                f[i][j][1] = std::max(f[i][j][1], f[i - 1][j][1] + val);
                if (j > 0) {
                    long long t = std::max(f[i - 1][j - 1][0], f[i - 1][j - 1][1]) + val;
                    f[i][j][1] = std::max(f[i][j][1], t);
                }
            }
        }
        return std::max(f[n][k][0], f[n][k][1]);
    }
};
