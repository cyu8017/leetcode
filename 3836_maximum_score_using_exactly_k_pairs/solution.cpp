// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

#include <algorithm>
#include <cstdint>
#include <limits>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& nums1, std::vector<int>& nums2, int K) {
        int n = (int)nums1.size(), m = (int)nums2.size();
        const int64_t NEG = std::numeric_limits<int64_t>::min() / 4;
        std::vector<std::vector<std::vector<int64_t>>> f(
            n + 1, std::vector<std::vector<int64_t>>(m + 1, std::vector<int64_t>(K + 1, NEG)));
        f[0][0][0] = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= K; k++) {
                    if (i > 0) f[i][j][k] = std::max(f[i][j][k], f[i - 1][j][k]);
                    if (j > 0) f[i][j][k] = std::max(f[i][j][k], f[i][j - 1][k]);
                    if (i > 0 && j > 0 && k > 0) {
                        f[i][j][k] = std::max(f[i][j][k],
                            f[i - 1][j - 1][k - 1] + (int64_t)nums1[i - 1] * nums2[j - 1]);
                    }
                }
            }
        }
        return f[n][m][K];
    }
};
