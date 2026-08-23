// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

#include <algorithm>
#include <climits>
#include <vector>
using namespace std;

class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        if (costs.empty()) {
            return 0;
        }
        int colorCount = costs[0].size();
        vector<int> previous = costs[0];
        for (size_t row = 1; row < costs.size(); row++) {
            int minCost = *min_element(previous.begin(), previous.end());
            int minIndex = min_element(previous.begin(), previous.end()) - previous.begin();
            int secondMin = INT_MAX;
            for (int color = 0; color < colorCount; color++) {
                if (color != minIndex) {
                    secondMin = min(secondMin, previous[color]);
                }
            }
            vector<int> current(colorCount);
            for (int color = 0; color < colorCount; color++) {
                int extra = color == minIndex ? secondMin : minCost;
                current[color] = costs[row][color] + extra;
            }
            previous = move(current);
        }
        return *min_element(previous.begin(), previous.end());
    }
};
