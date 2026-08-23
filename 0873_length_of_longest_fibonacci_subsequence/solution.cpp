// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int lenLongestFibSubseq(std::vector<int>& arr) {
        int n = static_cast<int>(arr.size());
        std::unordered_map<int, int> index;
        for (int i = 0; i < n; ++i) {
            index[arr[i]] = i;
        }
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 2));
        int ans = 0;
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < j; ++i) {
                auto it = index.find(arr[j] - arr[i]);
                if (it != index.end() && it->second < i) {
                    int k = it->second;
                    dp[i][j] = dp[k][i] + 1;
                    ans = std::max(ans, dp[i][j]);
                }
            }
        }
        return ans >= 3 ? ans : 0;
    }
};
