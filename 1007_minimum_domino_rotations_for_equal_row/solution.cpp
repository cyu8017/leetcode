// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minDominoRotations(std::vector<int>& tops, std::vector<int>& bottoms) {
        auto check = [&](int target) -> int {
            int rotTop = 0, rotBot = 0;
            for (int i = 0; i < static_cast<int>(tops.size()); ++i) {
                if (tops[i] != target && bottoms[i] != target) return INT_MAX;
                if (tops[i] != target) ++rotTop;
                if (bottoms[i] != target) ++rotBot;
            }
            return std::min(rotTop, rotBot);
        };
        int ans = std::min(check(tops[0]), check(bottoms[0]));
        return ans == INT_MAX ? -1 : ans;
    }
};

