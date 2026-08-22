// LeetCode 0342 - Power of Four
// https://leetcode.com/problems/power-of-four/

#include <stdbool.h>

bool isPowerOfFour(int n) {
    return n > 0 && (n & (n - 1)) == 0 && n % 3 == 1;
}
