// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minCost(int n, std::vector<int>& cuts) {
        std::vector<int> points;
        points.push_back(0);
        std::sort(cuts.begin(), cuts.end());
        points.insert(points.end(), cuts.begin(), cuts.end());
        points.push_back(n);
        const int size = static_cast<int>(points.size());
        std::vector<std::vector<int>> dp(size, std::vector<int>(size, 0));
        for (int width = 2; width < size; ++width) {
            for (int left = 0; left + width < size; ++left) {
                const int right = left + width;
                int best = INT_MAX;
                for (int mid = left + 1; mid < right; ++mid) {
                    best = std::min(best, dp[left][mid] + dp[mid][right]);
                }
                if (best == INT_MAX) {
                    best = 0;
                }
                dp[left][right] = best;
                if (right > left + 1) {
                    dp[left][right] += points[right] - points[left];
                }
            }
        }
        return dp[0][size - 1];
    }
};
