// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int numFactoredBinaryTrees(std::vector<int>& arr) {
        const int MOD = 1'000'000'007;
        std::sort(arr.begin(), arr.end());
        std::unordered_map<int, long long> dp;
        for (size_t i = 0; i < arr.size(); ++i) {
            int x = arr[i];
            long long ways = 1;
            for (size_t j = 0; j < i; ++j) {
                int left = arr[j];
                if (x % left == 0) {
                    int right = x / left;
                    if (dp.count(right)) {
                        ways = (ways + dp[left] * dp[right]) % MOD;
                    }
                }
            }
            dp[x] = ways;
        }
        long long ans = 0;
        for (auto& [_, v] : dp) {
            ans = (ans + v) % MOD;
        }
        return static_cast<int>(ans);
    }
};
