#include <vector>

class Solution {
public:
    int numOfArrays(int n, int m, int k) {
        const int mod = 1000000007;
        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(m + 1, 0));
        for (int maximum = 1; maximum <= m; ++maximum) dp[1][maximum] = 1;
        for (int len = 1; len < n; ++len) {
            std::vector<std::vector<int>> nxt(k + 1, std::vector<int>(m + 1, 0));
            for (int cost = 1; cost <= k; ++cost) {
                long long prefix = 0;
                for (int maximum = 1; maximum <= m; ++maximum) {
                    prefix = (prefix + dp[cost - 1][maximum - 1]) % mod;
                    nxt[cost][maximum] = (int)((1LL * maximum * dp[cost][maximum] + prefix) % mod);
                }
            }
            dp = std::move(nxt);
        }
        long long ans = 0;
        for (int x : dp[k]) ans = (ans + x) % mod;
        return (int)ans;
    }
};
