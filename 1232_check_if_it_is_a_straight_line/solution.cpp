// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

#include <vector>

class Solution {
public:
    bool checkStraightLine(std::vector<std::vector<int>>& coordinates) {
        int x0 = coordinates[0][0], y0 = coordinates[0][1];
        int dx = coordinates[1][0] - x0, dy = coordinates[1][1] - y0;
        for (int i = 2; i < static_cast<int>(coordinates.size()); ++i) {
            int x = coordinates[i][0], y = coordinates[i][1];
            if ((x - x0) * dy != (y - y0) * dx) {
                return false;
            }
        }
        return true;
    }
};
