// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

#include <stdbool.h>

static int rev2443(int x) {
    int r = 0;
    while (x > 0) {
        r = r * 10 + x % 10;
        x /= 10;
    }
    return r;
}

bool sumOfNumberAndReverse(int num) {
    for (int i = 0; i <= num; i++) {
        if (i + rev2443(i) == num) return true;
    }
    return false;
}
