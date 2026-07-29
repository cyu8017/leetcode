#include <string>
#include <vector>

class Solution {
public:
    int numberOfArrays(std::string s, int k) {
        const int mod = 1000000007;
        int n = (int)s.size();
        std::vector<int> dp(n + 1, 0);
        dp[n] = 1;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == '0') continue;
            long long value = 0;
            for (int j = i; j < n; ++j) {
                value = value * 10 + (s[j] - '0');
                if (value > k) break;
                dp[i] = (dp[i] + dp[j + 1]) % mod;
            }
        }
        return dp[0];
    }
};
