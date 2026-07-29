#include <algorithm>
#include <cstdlib>
#include <climits>
#include <vector>

class Solution {
public:
    int minDistance(std::vector<int>& houses, int k) {
        std::sort(houses.begin(), houses.end());
        int n = (int)houses.size();
        std::vector<std::vector<int>> cost(n, std::vector<int>(n, 0));
        for (int i = 0; i < n; ++i)
            for (int j = i; j < n; ++j) {
                int mid = houses[(i + j) / 2];
                for (int t = i; t <= j; ++t) cost[i][j] += std::abs(houses[t] - mid);
            }
        std::vector<long long> dp(n + 1, (long long)1e15);
        dp[0] = 0;
        for (int mb = 0; mb < k; ++mb) {
            std::vector<long long> ndp(n + 1, (long long)1e15);
            ndp[0] = 0;
            for (int j = 1; j <= n; ++j)
                for (int i = 0; i < j; ++i)
                    ndp[j] = std::min(ndp[j], dp[i] + cost[i][j - 1]);
            dp = std::move(ndp);
        }
        return (int)dp[n];
    }
};
