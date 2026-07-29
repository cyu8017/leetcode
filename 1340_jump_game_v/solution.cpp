#include <algorithm>
#include <vector>

class Solution {
public:
    int maxJumps(std::vector<int>& arr, int d) {
        int n = (int)arr.size();
        std::vector<int> dp(n, 1);
        std::vector<std::pair<int, int>> order;
        for (int i = 0; i < n; ++i) order.push_back({arr[i], i});
        std::sort(order.begin(), order.end());
        for (auto [_, i] : order) {
            for (int step : {-1, 1}) {
                int j = i + step;
                while (j >= 0 && j < n && std::abs(j - i) <= d && arr[j] < arr[i]) {
                    dp[i] = std::max(dp[i], 1 + dp[j]);
                    j += step;
                }
            }
        }
        return *std::max_element(dp.begin(), dp.end());
    }
};
