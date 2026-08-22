// LeetCode 0365 - Water and Jug Problem
// https://leetcode.com/problems/water-and-jug-problem/

#include <stdbool.h>

static int gcd(int a, int b) {
    while (b != 0) {
        int remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}

bool canMeasureWater(int x, int y, int target) {
    if (target == 0) {
        return true;
    }
    if (x + y < target) {
        return false;
    }
    return target % gcd(x, y) == 0;
}
