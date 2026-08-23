// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

#include <climits>
#include <vector>

class Solution {
public:
    long long maximumScore(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> a = nums;
        a.insert(a.end(), nums.begin(), nums.end());
        if (k > n) k = n;
        long long best = 0;
        const long long NEG = -(1LL << 60);
        for (int start = 0; start < n; start++) {
            std::vector<int> seg(a.begin() + start, a.begin() + start + n);
            std::vector<std::vector<long long>> dp(n + 1, std::vector<long long>(k + 1, NEG));
            dp[0][0] = 0;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= k && j <= i; j++) {
                    long long mx = NEG;
                    for (int t = i; t >= j; t--) {
                        if (seg[t - 1] > mx) mx = seg[t - 1];
                        if (dp[t - 1][j - 1] > NEG) {
                            long long cand = dp[t - 1][j - 1] + mx;
                            if (cand > dp[i][j]) dp[i][j] = cand;
                        }
                    }
                }
            }
            if (dp[n][k] > best) best = dp[n][k];
        }
        return best;
    }
};
