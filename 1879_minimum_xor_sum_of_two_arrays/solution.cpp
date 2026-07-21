// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minimumXORSum(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = static_cast<int>(nums1.size());
        std::vector<int> dp(1 << n, INT_MAX / 2);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int i = 0;
            for (int tmp = mask; tmp; tmp &= tmp - 1) {
                i++;
            }
            if (i >= n) continue;
            for (int j = 0; j < n; j++) {
                if (mask & (1 << j)) continue;
                int nextMask = mask | (1 << j);
                int cost = dp[mask] + (nums1[i] ^ nums2[j]);
                if (cost < dp[nextMask]) {
                    dp[nextMask] = cost;
                }
            }
        }
        return dp[(1 << n) - 1];
    }
};
