// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

#include <string>
#include <vector>

class Solution {
public:
    int beautifulPartitions(std::string s, int k, int minLength) {
        const int mod = 1000000007;
        auto isPrime = [](char c) {
            return c == '2' || c == '3' || c == '5' || c == '7';
        };
        int n = (int)s.size();
        if (!isPrime(s[0]) || isPrime(s[n - 1])) return 0;
        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n + 1));
        dp[0][0] = 1;
        for (int p = 1; p <= k; p++) {
            int pref = 0, j = 0;
            for (int i = 1; i <= n; i++) {
                while (j <= i - minLength) {
                    if (j == 0 || (isPrime(s[j]) && !isPrime(s[j - 1]))) {
                        pref = (pref + dp[p - 1][j]) % mod;
                    }
                    j++;
                }
                if (!isPrime(s[i - 1])) dp[p][i] = pref;
            }
        }
        return dp[k][n];
    }
};
