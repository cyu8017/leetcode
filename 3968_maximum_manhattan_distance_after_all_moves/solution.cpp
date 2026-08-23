// LeetCode 3968 - Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

#include <cmath>
#include <string>

class Solution {
public:
    int maxDistance(std::string moves) {
        int x = 0, y = 0, z = 0;
        for (char c : moves) {
            if (c == 'U') x -= 1;
            else if (c == 'D') x += 1;
            else if (c == 'L') y -= 1;
            else if (c == 'R') y += 1;
            else z += 1;
        }
        return std::abs(x) + std::abs(y) + z;
    }
};
