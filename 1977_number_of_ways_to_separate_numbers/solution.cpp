// LeetCode 1977 - Number of Ways to Separate Numbers
#include <string>
#include <vector>

class Solution {
public:
    int numberOfCombinations(std::string num) {
        const int MOD = 1000000007;
        int n = (int)num.size();
        if (num[0] == '0') return 0;
        std::vector<std::vector<int>> lcp(n + 1, std::vector<int>(n + 1, 0));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (num[i] == num[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1;
            }
        }
        auto le = [&](int a, int b, int length) {
            int common = lcp[a][b];
            if (common >= length) return true;
            return num[a + common] < num[b + common];
        };
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(n + 1, 0));
        std::vector<std::vector<int>> pref(n + 1, std::vector<int>(n + 1, 0));
        for (int i = 1; i <= n; i++) {
            for (int l = 1; l <= i; l++) {
                int start = i - l;
                if (num[start] == '0') dp[i][l] = 0;
                else if (start == 0) dp[i][l] = 1;
                else {
                    int ways = l > 1 ? pref[start][std::min(l - 1, start)] : 0;
                    if (start >= l && le(start - l, start, l)) ways = (ways + dp[start][l]) % MOD;
                    dp[i][l] = ways;
                }
            }
            for (int l = 1; l <= n; l++) {
                pref[i][l] = (pref[i][l - 1] + (l <= i ? dp[i][l] : 0)) % MOD;
            }
        }
        return pref[n][n];
    }
};
