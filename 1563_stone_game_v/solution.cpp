// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/

#include <algorithm>
#include <vector>

class Solution {
public:
    int stoneGameV(std::vector<int>& stoneValue) {
        const int n = static_cast<int>(stoneValue.size());
        if (n == 0) {
            return 0;
        }
        std::vector<int> pre(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pre[i + 1] = pre[i] + stoneValue[i];
        }
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        std::vector<std::vector<int>> left(n, std::vector<int>(n, 0));
        std::vector<std::vector<int>> right(n, std::vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            left[i][i] = right[i][i] = stoneValue[i];
        }
        for (int length = 2; length <= n; ++length) {
            for (int i = 0; i + length - 1 < n; ++i) {
                const int j = i + length - 1;
                int lo = i;
                int hi = j - 1;
                while (lo <= hi) {
                    const int mid = lo + (hi - lo) / 2;
                    if (2 * (pre[mid + 1] - pre[i]) >= pre[j + 1] - pre[i]) {
                        hi = mid - 1;
                    } else {
                        lo = mid + 1;
                    }
                }
                const int split = lo;
                const int left_sum = pre[split + 1] - pre[i];
                const int right_sum = pre[j + 1] - pre[split + 1];
                int best = right[split + 1][j];
                if (left_sum == right_sum) {
                    best = std::max(best, left[i][split]);
                } else if (split > i) {
                    best = std::max(best, left[i][split - 1]);
                }
                dp[i][j] = best;
                const int total = pre[j + 1] - pre[i];
                left[i][j] = std::max(left[i][j - 1], total + best);
                right[i][j] = std::max(right[i + 1][j], total + best);
            }
        }
        return dp[0][n - 1];
    }
};
