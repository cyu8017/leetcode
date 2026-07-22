// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

#include <queue>
#include <vector>

class Solution {
public:
    int furthestBuilding(std::vector<int>& heights, int bricks, int ladders) {
        std::priority_queue<int, std::vector<int>, std::greater<>> climbs;
        for (int i = 0; i + 1 < static_cast<int>(heights.size()); ++i) {
            const int d = heights[i + 1] - heights[i];
            if (d <= 0) {
                continue;
            }
            climbs.push(d);
            if (static_cast<int>(climbs.size()) > ladders) {
                bricks -= climbs.top();
                climbs.pop();
            }
            if (bricks < 0) {
                return i;
            }
        }
        return static_cast<int>(heights.size()) - 1;
    }
};
