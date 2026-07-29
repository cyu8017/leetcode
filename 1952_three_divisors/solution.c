// LeetCode 1952 - Three Divisors
// https://leetcode.com/problems/three-divisors/

#include <stdbool.h>
#include <math.h>

bool isThree(int n) {
    int root = (int)sqrt((double)n);
    if (root * root != n) return false;
    if (root < 2) return false;
    for (int i = 2; i * i <= root; i++) {
        if (root % i == 0) return false;
    }
    return true;
}
