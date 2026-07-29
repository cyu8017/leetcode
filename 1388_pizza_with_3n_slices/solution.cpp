#include <algorithm>
#include <vector>

class Solution {
    int line(const std::vector<int>& a, int k) {
        int n = (int)a.size();
        std::vector<std::vector<int>> dp(n + 2, std::vector<int>(k + 1, 0));
        for (int i = 0; i < n; ++i)
            for (int j = 1; j <= k; ++j)
                dp[i + 2][j] = std::max(dp[i + 1][j], dp[i][j - 1] + a[i]);
        return dp[n + 1][k];
    }
public:
    int maxSizeSlices(std::vector<int>& slices) {
        int k = (int)slices.size() / 3;
        std::vector<int> a(slices.begin(), slices.end() - 1);
        std::vector<int> b(slices.begin() + 1, slices.end());
        return std::max(line(a, k), line(b, k));
    }
};
