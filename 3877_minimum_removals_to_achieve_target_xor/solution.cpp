// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minRemovals(std::vector<int>& nums, int target) {
        int mx = *std::max_element(nums.begin(), nums.end());
        int m = 0;
        if (mx > 0) {
            unsigned int u = (unsigned int)mx;
            while (u) {
                m++;
                u >>= 1;
            }
        }
        if ((1 << m) <= target) return -1;

        int n = (int)nums.size();
        int N = 1 << m;
        std::vector<std::vector<int>> f(n + 1, std::vector<int>(N, INT_MIN));
        f[0][0] = 0;

        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            for (int j = 0; j < N; j++) {
                f[i][j] = f[i - 1][j];
                if (f[i - 1][j ^ x] != INT_MIN) {
                    f[i][j] = std::max(f[i][j], f[i - 1][j ^ x] + 1);
                }
            }
        }

        if (f[n][target] < 0) return -1;
        return n - f[n][target];
    }
};
