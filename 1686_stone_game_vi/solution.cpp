// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int stoneGameVI(std::vector<int>& aliceValues, std::vector<int>& bobValues) {
        int n = static_cast<int>(aliceValues.size());
        std::vector<int> order(n);
        std::iota(order.begin(), order.end(), 0);
        std::sort(order.begin(), order.end(), [&](int i, int j) {
            return aliceValues[i] + bobValues[i] > aliceValues[j] + bobValues[j];
        });
        int score = 0;
        for (int t = 0; t < n; ++t) {
            int i = order[t];
            if (t % 2 == 0) {
                score += aliceValues[i];
            } else {
                score -= bobValues[i];
            }
        }
        return (score > 0) - (score < 0);
    }
};
