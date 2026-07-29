#include <algorithm>
#include <climits>
#include <string>
#include <vector>

class Solution {
public:
    std::string stoneGameIII(std::vector<int>& stoneValue) {
        int n = (int)stoneValue.size();
        std::vector<long long> dp(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            long long take = 0;
            dp[i] = LLONG_MIN / 4;
            for (int j = i; j < std::min(i + 3, n); ++j) {
                take += stoneValue[j];
                dp[i] = std::max(dp[i], take - dp[j + 1]);
            }
        }
        if (dp[0] > 0) return "Alice";
        if (dp[0] < 0) return "Bob";
        return "Tie";
    }
};
