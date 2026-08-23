// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty()) {
            return 0;
        }
        vector<int> previous = costs[0];
        for (size_t row = 1; row < costs.size(); row++) {
            vector<int> next = {
                costs[row][0] + min(previous[1], previous[2]),
                costs[row][1] + min(previous[0], previous[2]),
                costs[row][2] + min(previous[0], previous[1]),
            };
            previous = move(next);
        }
        return min({previous[0], previous[1], previous[2]});
    }
};
