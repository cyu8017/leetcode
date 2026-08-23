// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumLines(std::vector<std::vector<int>>& stockPrices) {
        if (stockPrices.size() <= 1) return 0;
        std::sort(stockPrices.begin(), stockPrices.end());
        int ans = 1;
        for (size_t i = 2; i < stockPrices.size(); ++i) {
            long long x0 = stockPrices[i-2][0], y0 = stockPrices[i-2][1];
            long long x1 = stockPrices[i-1][0], y1 = stockPrices[i-1][1];
            long long x2 = stockPrices[i][0], y2 = stockPrices[i][1];
            if ((y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0)) ans++;
        }
        return ans;
    }
};
