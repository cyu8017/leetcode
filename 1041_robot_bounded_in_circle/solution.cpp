// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

#include <string>

class Solution {
public:
    bool isRobotBounded(std::string instructions) {
        int x = 0, y = 0, dx = 0, dy = 1;
        for (char ch : instructions) {
            if (ch == 'G') {
                x += dx;
                y += dy;
            } else if (ch == 'L') {
                int ndx = -dy, ndy = dx;
                dx = ndx;
                dy = ndy;
            } else {
                int ndx = dy, ndy = -dx;
                dx = ndx;
                dy = ndy;
            }
        }
        return (x == 0 && y == 0) || !(dx == 0 && dy == 1);
    }
};

