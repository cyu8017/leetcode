// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> numMovesStones(int a, int b, int c) {
        int x = std::min({a, b, c});
        int z = std::max({a, b, c});
        int y = a + b + c - x - z;
        int minMoves;
        if (z - x == 2) minMoves = 0;
        else if (y - x <= 2 || z - y <= 2) minMoves = 1;
        else minMoves = 2;
        return {minMoves, z - x - 2};
    }
};

