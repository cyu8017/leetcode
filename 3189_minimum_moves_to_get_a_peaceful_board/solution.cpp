// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

#include <vector>
#include <algorithm>
#include <cstdlib>

class Solution {
public:
    int minMoves(std::vector<std::vector<int>>& rooks) {
        int ans = 0;
        std::sort(rooks.begin(), rooks.end(), [](auto& a, auto& b) { return a[0] < b[0]; });
        for (int i = 0; i < (int)rooks.size(); i++) ans += std::abs(rooks[i][0] - i);
        std::sort(rooks.begin(), rooks.end(), [](auto& a, auto& b) { return a[1] < b[1]; });
        for (int j = 0; j < (int)rooks.size(); j++) ans += std::abs(rooks[j][1] - j);
        return ans;
    }
};
