// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

#include <stdbool.h>

bool isRobotBounded(char* instructions) {
    int x = 0, y = 0, dx = 0, dy = 1;
    for (char* p = instructions; *p; p++) {
        if (*p == 'G') {
            x += dx;
            y += dy;
        } else if (*p == 'L') {
            int ndx = -dy, ndy = dx;
            dx = ndx; dy = ndy;
        } else {
            int ndx = dy, ndy = -dx;
            dx = ndx; dy = ndy;
        }
    }
    return (x == 0 && y == 0) || !(dx == 0 && dy == 1);
}
