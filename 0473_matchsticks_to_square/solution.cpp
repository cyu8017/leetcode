// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
    bool dfs(int index, int side, std::vector<int>& matchsticks, std::vector<int>& sides) {
        if (index == static_cast<int>(matchsticks.size())) {
            return sides[0] == side && sides[1] == side && sides[2] == side && sides[3] == side;
        }

        const int length = matchsticks[index];
        for (int sideIndex = 0; sideIndex < 4; ++sideIndex) {
            if (sides[sideIndex] + length > side) {
                continue;
            }
            if (sideIndex > 0 && sides[sideIndex] == sides[sideIndex - 1]) {
                continue;
            }
            sides[sideIndex] += length;
            if (dfs(index + 1, side, matchsticks, sides)) {
                return true;
            }
            sides[sideIndex] -= length;
        }
        return false;
    }

public:
    bool makesquare(std::vector<int>& matchsticks) {
        if (matchsticks.empty()) {
            return false;
        }
        const int total = std::accumulate(matchsticks.begin(), matchsticks.end(), 0);
        if (total % 4 != 0) {
            return false;
        }
        const int side = total / 4;
        std::sort(matchsticks.begin(), matchsticks.end(), std::greater<int>());
        std::vector<int> sides(4, 0);
        return dfs(0, side, matchsticks, sides);
    }
};
