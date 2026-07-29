#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minInsertions(std::string s) {
        int n = (int)s.size();
        std::string rev = s;
        std::reverse(rev.begin(), rev.end());
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(n + 1, 0));
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
                dp[i][j] = s[i - 1] == rev[j - 1] ? dp[i - 1][j - 1] + 1 : std::max(dp[i - 1][j], dp[i][j - 1]);
        return n - dp[n][n];
    }
};
