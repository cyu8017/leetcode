// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

#include <stdbool.h>
#include <stdlib.h>

bool escapeGhosts(int** ghosts, int ghostsSize, int* ghostsColSize, int* target, int targetSize) {
    (void)ghostsColSize;
    (void)targetSize;
    int dist = abs(target[0]) + abs(target[1]);
    for (int i = 0; i < ghostsSize; i++) {
        int g = abs(ghosts[i][0] - target[0]) + abs(ghosts[i][1] - target[1]);
        if (g <= dist) return false;
    }
    return true;
}
