// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

#include <vector>

class Solution {
public:
    int sumOfPower(std::vector<int>& nums, int k) {
        const int mod = 1e9 + 7;
        int n = (int)nums.size();
        std::vector<std::vector<int>> f(n + 1, std::vector<int>(k + 1, 0));
        f[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                f[i][j] = (f[i - 1][j] * 2LL) % mod;
                if (j >= nums[i - 1])
                    f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % mod;
            }
        }
        return f[n][k];
    }
};
