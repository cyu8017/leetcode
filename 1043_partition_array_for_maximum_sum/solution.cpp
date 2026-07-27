// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxSumAfterPartitioning(std::vector<int>& arr, int k) {
        int n = static_cast<int>(arr.size());
        std::vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            int best = 0;
            for (int size = 1; size <= std::min(k, i); ++size) {
                best = std::max(best, arr[i - size]);
                dp[i] = std::max(dp[i], dp[i - size] + best * size);
            }
        }
        return dp[n];
    }
};

