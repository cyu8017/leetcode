// LeetCode 3968 - Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

#include <stdlib.h>

int maxDistance(char* moves) {
    int x = 0, y = 0, z = 0;
    for (int i = 0; moves[i]; i++) {
        char c = moves[i];
        if (c == 'U') x -= 1;
        else if (c == 'D') x += 1;
        else if (c == 'L') y -= 1;
        else if (c == 'R') y += 1;
        else z += 1;
    }
    if (x < 0) x = -x;
    if (y < 0) y = -y;
    return x + y + z;
}
