// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

#include <array>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& a, std::vector<int>& b) {
        const long long neg = -(1LL << 62);
        std::array<long long, 5> dp{0, neg, neg, neg, neg};
        for (int x : b) {
            for (int k = 4; k >= 1; k--) {
                if (dp[k - 1] == neg) continue;
                long long v = dp[k - 1] + (long long)a[k - 1] * x;
                if (v > dp[k]) dp[k] = v;
            }
        }
        return dp[4];
    }
};
