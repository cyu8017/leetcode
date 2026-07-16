// LeetCode 0096 - Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

#include <vector>

class Solution {
public:
    int numTrees(int n) {
        std::vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int nodes = 1; nodes <= n; ++nodes) {
            for (int root = 1; root <= nodes; ++root) {
                dp[nodes] += dp[root - 1] * dp[nodes - root];
            }
        }
        return dp[n];
    }
};
