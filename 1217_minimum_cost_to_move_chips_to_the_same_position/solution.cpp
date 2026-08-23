// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minCostToMoveChips(std::vector<int>& position) {
        int odd = 0;
        for (int x : position) {
            odd += x & 1;
        }
        return std::min(odd, static_cast<int>(position.size()) - odd);
    }
};
