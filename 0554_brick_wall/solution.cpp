// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int leastBricks(std::vector<std::vector<int>>& wall) {
        std::unordered_map<int, int> edges;
        int best = 0;
        for (const auto& row : wall) {
            int width = 0;
            for (std::size_t i = 0; i + 1 < row.size(); ++i) {
                width += row[i];
                best = std::max(best, ++edges[width]);
            }
        }
        return static_cast<int>(wall.size()) - best;
    }
};
