// LeetCode 0657 - Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/

#include <stdbool.h>

bool judgeCircle(char* moves) {
    int x = 0, y = 0;
    for (char* p = moves; *p; p++) {
        if (*p == 'U') {
            y++;
        } else if (*p == 'D') {
            y--;
        } else if (*p == 'L') {
            x--;
        } else if (*p == 'R') {
            x++;
        }
    }
    return x == 0 && y == 0;
}
