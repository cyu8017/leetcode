// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

#include <vector>

class Solution {
public:
    int kInversePairs(int n, int k) {
        constexpr int mod = 1000000007;
        std::vector<int> dp(k + 1);
        dp[0] = 1;
        for (int size = 1; size <= n; ++size) {
            std::vector<int> nxt(k + 1);
            long long prefix = 0;
            for (int pairs = 0; pairs <= k; ++pairs) {
                prefix = (prefix + dp[pairs]) % mod;
                if (pairs >= size) {
                    prefix = (prefix - dp[pairs - size] + mod) % mod;
                }
                nxt[pairs] = static_cast<int>(prefix);
            }
            dp.swap(nxt);
        }
        return dp[k];
    }
};
