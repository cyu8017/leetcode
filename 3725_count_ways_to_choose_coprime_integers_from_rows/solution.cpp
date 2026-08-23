// LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

#include <numeric>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int countCoprime(std::vector<std::vector<int>>& mat) {
        const int MOD = 1000000007;
        int m = (int)mat.size();
        std::unordered_map<int, int> dp;
        for (int v : mat[0]) dp[v]++;
        for (int i = 1; i < m; i++) {
            std::unordered_map<int, int> ndp;
            for (int v : mat[i]) {
                for (auto& [g, cnt] : dp) {
                    int ng = std::gcd(g, v);
                    ndp[ng] = (ndp[ng] + cnt) % MOD;
                }
            }
            dp.swap(ndp);
        }
        return dp[1];
    }
};
