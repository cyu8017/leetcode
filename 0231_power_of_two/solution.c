// LeetCode 0231 - Power of Two
// https://leetcode.com/problems/power-of-two/

#include <stdbool.h>

bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}
