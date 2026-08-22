// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

#include <stdbool.h>

bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
    int dx = sx - fx; if (dx < 0) dx = -dx;
    int dy = sy - fy; if (dy < 0) dy = -dy;
    int need = dx > dy ? dx : dy;
    if (need == 0) return t != 1;
    return t >= need;
}
