// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/

#include <stdbool.h>

static int gcd2543(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

bool isReachable(int targetX, int targetY) {
    int g = gcd2543(targetX, targetY);
    while (g % 2 == 0) g /= 2;
    return g == 1;
}
